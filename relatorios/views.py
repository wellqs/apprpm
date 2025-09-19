# relatorios/views.py

import os
import requests
import markdown2
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from zoneinfo import ZoneInfo
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from .forms import NSSForm, SESMTForm
from .models import Relatorio
from weasyprint import HTML

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


@login_required
def home_view(request):
    user_profile = request.user.profile
    form = None

    if user_profile.especialidade == 'NSS':
        form = NSSForm(request.POST or None)
    elif user_profile.especialidade == 'SESMT':
        form = SESMTForm(request.POST or None)

    if request.method == 'POST' and form and form.is_valid():
        data_to_send = {key: value for key, value in form.cleaned_data.items()}
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            prompt_text = f"""
            Aja como um especialista em Segurança e Saúde do Trabalho (SST).
            Gere um Relatório de Produtividade Mensal formal e bem estruturado.
            A parte principal do relatório deve ser uma tabela em formato Markdown com as colunas "Atividade", "Quantidade" e "Descrição".
            Na coluna "Descrição", crie uma frase curta sobre a atividade realizada.
            **Exemplo de formato da tabela:**
            | Atividade | Quantidade | Descrição |
            |---|---|---|
            | Investigação de Acidentes | 1 | Realizada 1 investigação de acidente para análise de causas. |
            | Análise de Relatórios | 5 | Foram analisados 5 relatórios de empresas terceirizadas. |
            **Use os seguintes dados para preencher a tabela:**
            {data_to_send}
            Finalize o relatório com um parágrafo de conclusão e um campo para assinatura.
            """

            completion = client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "system", "content": "Você é um assistente que gera relatórios de produtividade."},
                {"role": "user", "content": prompt_text}
              ]
            )

            report_text = completion.choices[0].message.content
            report_html = markdown2.markdown(report_text, extras=["tables"])

            Relatorio.objects.create(
                usuario=request.user,
                especialidade=user_profile.especialidade,
                report_html=report_html
            )

            now = datetime.now(ZoneInfo("America/Porto_Velho"))
            formatted_time = now.strftime("%d/%m/%Y às %H:%M:%S")

            context = {
                'report_html': report_html,
                'generation_time': formatted_time
            }
            return render(request, 'resultado.html', context)

        except Exception as e:
            error_message = f"Ocorreu um erro ao chamar a API da OpenAI: {e}"
            return render(request, 'home.html', {'form': form, 'error': error_message})

    return render(request, 'home.html', {'form': form})


@login_required
def historico_view(request):
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    relatorios_list = Relatorio.objects.filter(usuario=request.user)

    if data_inicio:
        relatorios_list = relatorios_list.filter(data_criacao__date__gte=data_inicio)
    if data_fim:
        relatorios_list = relatorios_list.filter(data_criacao__date__lte=data_fim)

    context = {
        'relatorios': relatorios_list
    }
    return render(request, 'historico.html', context)


@require_POST
def gerar_pdf_view(request):
    html = request.POST.get('report_html', '')
    time_str = request.POST.get('generation_time', '')

    html_string = render_to_string('relatorio_pdf.html', {
        'report_html': html,
        'generation_time': time_str
    })

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
    return response


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')