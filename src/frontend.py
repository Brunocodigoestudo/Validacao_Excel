import streamlit as st


class ExcelValidorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validador de Schema Excel"
        )

    def display_header(self):
        st.title("Validador de Schema Excel")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

    def display_results(self, result, error):
        if error:
            st.error(f"Erro na Validação: {error}")
        else:
            st.success("A estrtura do Excel está correta!")
