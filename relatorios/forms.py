# relatorios/forms.py

from django import forms

class NSSForm(forms.Form):
    # [cite_start]Campos baseados na tabela ATIVIDADES DO NÚCLEO DE SAÚDE DO SERVIDOR - NSS [cite: 10]
    acompanhamento_readaptacao = forms.IntegerField(label="1. Acompanhamento no Processo Readaptação/Reabilitação", initial=0)
    acompanhamento_acidentes_trabalho_nss = forms.IntegerField(label="2. Acompanhamento/Orientação em Acidentes de Trabalho", initial=0)
    agendamento_exames = forms.IntegerField(label="3. Agendamento/Solicitação de Exames Diversos pela Unidade", initial=0)
    consultas_eventuais = forms.IntegerField(label="4. Consultas Eventuais (demanda da unidade)", initial=0)
    consultas_medicas_ocupacionais = forms.IntegerField(label="5. Consultas Médicas Ocupacionais (ASO)", initial=0)
    elaboracao_documentos_nss = forms.IntegerField(label="6. Elaboração de Memorandos, Oficios e Documentos em Geral", initial=0)
    elaboracao_palestras_nss = forms.IntegerField(label="7. Elaboração de Palestras, Cursos, Informativos e Materiais de Formação", initial=0)
    elaboracao_pareceres = forms.IntegerField(label="8. Elaboração de Pareceres em Saúde do Trabalhador", initial=0)
    elaboracao_programas_saude = forms.IntegerField(label="9. Elaboração/ Realização de Programas de Saúde do Trabalho", initial=0)
    orientacoes_tecnicas_nss = forms.IntegerField(label="10. Orientações Técnicas/Informações aos Servidores e Setores", initial=0)
    participacao_reunioes_nss = forms.IntegerField(label="11. Participações em Reuniões, Palestras, Treinamentos e Eventos", initial=0)
    promocao_reunioes_nss = forms.IntegerField(label="12. Promoção de Reuniões, Palestras, Treinamentos e Eventos", initial=0)
    realizacao_aso = forms.IntegerField(label="13. Realização/conclusão de ASO", initial=0)
    regulacao_exames_sisreg = forms.IntegerField(label="14. Regulação de Exames e Consultas de Especialidades (SISREG)", initial=0)
    visitas_externas_nss = forms.IntegerField(label="15. Visitas Externas Multidisciplinares ao Servidor ou à unidades de saúde", initial=0)


class SESMTForm(forms.Form):
    # [cite_start]Campos baseados na tabela ATIVIDADES DE SEGURANÇA DO TRABALHO - SESMT [cite: 13]
    investigacao_acidentes_riat = forms.IntegerField(label="1. Acompanhamento/Investigação em Acidentes com elaboração do RIAT", initial=0)
    analise_relatorios_terceirizadas = forms.IntegerField(label="2. Análise de Relatórios e Programas de Saúde e Segurança de Terceirizadas", initial=0)
    aplicacao_dds = forms.IntegerField(label="3. Aplicação de Diálogos Diários de Segurança - DDS", initial=0)
    avaliacao_ambientes = forms.IntegerField(label="4. Avaliação Quantitativa/Qualitativa de Ambientes", initial=0)
    elaboracao_sinalizacoes = forms.IntegerField(label="5. Elaboração de Artes e Instalações de Sinalizações Gráficas", initial=0)
    elaboracao_documentos_sesmt = forms.IntegerField(label="6. Elaboração de Memorandos, Oficios e Documentos em Geral", initial=0)
    elaboracao_palestras_sesmt = forms.IntegerField(label="7. Elaboração de Palestras, POPs, Ordem de serviços, Cursos, etc.", initial=0)
    elaboracao_programas_seguranca = forms.IntegerField(label="8. Elaboração/Atualização de Programas de Segurança do Trabalho", initial=0)
    cautelagem_epi = forms.IntegerField(label="9. Cautelagem de EPI com Instruções de Uso, Guarda e Conservação", initial=0)
    orientacoes_tecnicas_sesmt = forms.IntegerField(label="10. Orientações Técnicas/Informações a Servidores e Setores", initial=0)
    participacao_reunioes_sesmt = forms.IntegerField(label="11. Participações em Reuniões, Palestras, Treinamentos e Eventos", initial=0)
    promocao_reunioes_sesmt = forms.IntegerField(label="12. Promoção de Reuniões, Palestras, Treinamentos e Eventos", initial=0)
    servicos_tecnicos_checklist = forms.IntegerField(label="13. Serviços Técnicos (check-list e acompanhamentos)", initial=0)