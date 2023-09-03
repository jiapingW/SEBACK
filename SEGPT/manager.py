from segpt.roles.product_manager import ProductManager
from segpt.roles.architect import Architect
from segpt.roles.project_manager import ProjectManager
from segpt.roles.engineer import Engineer
from segpt.roles.unit_tester import Tester
from langchain.chat_models import AzureChatOpenAI
from segpt.roles.architect_engineer import Architect_Engineer

import os
from langchain.retrievers import ContextualCompressionRetriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from settings import API_KEY, API_TYPE, API_VERSION, DEPLOYMENT_NAME, BASE_URL
from segpt.roles.requirement_engineer import RequirementEngineer


class Manager:
    def __init__(self):
        # Initialize other roles
        self.product_manager = ProductManager()
        self.requirement_engineer = RequirementEngineer()
        self.architect = Architect()
        self.project_manager = ProjectManager()
        self.engineer = Engineer()
        self.tester = Tester()
        self.architect_engineer = Architect_Engineer()
        self.model = AzureChatOpenAI(
            openai_api_base=BASE_URL,
            openai_api_version=API_VERSION,
            deployment_name=DEPLOYMENT_NAME,
            openai_api_key=API_KEY,
            openai_api_type=API_TYPE,
        )
        self.project_name = "workspace/finance_tracker"
        
        self.embeddings = OpenAIEmbeddings(
            openai_api_base="https://wjp-gpt3.openai.azure.com/",
            openai_api_version=API_VERSION,
            openai_api_key="7903f0912b9e4626bcb5412830524a83",
            openai_api_type=API_TYPE,
            deployment="text-embedding-ada-002"
        )

    def _load_documents_from_directory(self):
        files = []
        for dirpath, _, filenames in os.walk(self.project_name):
            for f in filenames:
                files.append(os.path.join(dirpath, f))
        documents = []
        for file in files:
            documents.extend(TextLoader(file).load())
        return documents

    def getrelevant(self, feedback):
        self.documents = self._load_documents_from_directory()
        self.retriever = FAISS.from_documents(self.documents, self.embeddings).as_retriever()
        # EmbeddingsFilter initialization
        embeddings_filter = EmbeddingsFilter(embeddings=self.embeddings, similarity_threshold=0.76)  # You can adjust the threshold as per your requirements

        # Contextual compression with EmbeddingsFilter
        compression_retriever = ContextualCompressionRetriever(base_compressor=embeddings_filter, base_retriever=self.retriever)
        relevant_docs = compression_retriever.get_relevant_documents(feedback)
        
        # Return relevant content
        return [doc.page_content for doc in relevant_docs]

    def start_project(self, idea):
        # Initial steps
        self.product_manager.write_prd(idea)
        self.requirement_engineer.write_req()
        self.architect.write_design()
        # Gather feedback from the user
        feedback = input("Are you satisfied with the design? (yes/no): ")
        
        while feedback.lower() != 'yes':
            detailed_feedback = input("Please provide feedback for improvements: ")
            choice = input("Do you want to rework from 'prd.md', 'requirement.md' or 'system_design.md'? Enter 'prd', 'require' or 'design': ")

            if choice == 'prd':
                self.product_manager.rewrite_prd(detailed_feedback)
                self.requirement_engineer.rewrite_req(detailed_feedback)
                self.architect.rewrite_design(detailed_feedback)
            elif choice == 'require':
                self.requirement_engineer.rewrite_req(detailed_feedback)
                self.architect.rewrite_design(detailed_feedback)
            elif choice == 'design':
                self.architect.rewrite_design(detailed_feedback)
            else:
                print("Invalid choice. Defaulting to rewriteing from 'prd.md'.")
                self.product_manager.rewrite_prd(detailed_feedback)
                self.requirement_engineer.rewrite_req(detailed_feedback)
                self.architect.rewrite_design(detailed_feedback)
            
            feedback = input("Are you satisfied with the revised design? (yes/no): ")
        
        self.architect_engineer.write_detail()
        self.project_manager.write_task()
        self.engineer.write_code()
        # self.tester.write_test(self.engineer.filelist)
        # If the user is satisfied, proceed with the subsequent steps
        # tasks = self.project_manager.write_tasks(design)
        # code = self.engineer.write_code(tasks)
        
        # 整体不满意暂不加入修改
        # feedback = input("Are you satisfied with the design? (yes/no): ")
        # while feedback.lower() != 'yes':
        #     detailed_feedback = input("Please provide feedback for improvements: ")

        #     recommendation = choose_role(detailed_feedback)
            
        #     # Depending on the recommendation, revisit the appropriate step
        #     if recommendation == 'ProductManager':
        #         prd = self.product_manager.rework_prd(detailed_feedback)
        #     if recommendation == 'Architect' or recommendation == 'ProductManager':
        #         design = self.architect.rework_design(prd)
        #     if recommendation == 'ProjectManager' or recommendation == 'Architect' or recommendation == 'ProductManager':
        #         tasks = self.project_manager.rework_tasks(design)
        #     code = self.engineer.rework_code(tasks)
        #     # ... [Handle other roles similarly]
            
        #     feedback = input("Are you satisfied with the revised project outcome? (yes/no): ")
     
        # return code

    def start_project_from_engineer(self):
        self.architect_engineer.write_detail()
        self.project_manager.write_task()
        self.engineer.write_code()

if __name__ == '__main__':
    manager = Manager()
    relevant = manager.getrelevant("what is the user story?")
    print(relevant)