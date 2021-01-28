# include <iostream>
# include <stdlib.h>
using namespace std;

int main(){
	string nome_entrada, nome_saida;
	cout<<"--------------------------------------------------------------------------------\n";
	cout<<"|\t\t\tAutor: Lucas Macedo da Silva \t\t\t\t|\n";
	cout<<"|\t\t\tVersão 1.1 \t\t\t\t\t\t|\n";
	cout<<"--------------------------------------------------------------------------------\n";

	cout<<"\n\nConversor de jupyter para PDF e script\n\n";
	
	
	int opc;
	
	do{
		cout<<"\n[1] De jupyter para PDF\n[2] De jupyter para script\n[0] Para sair\nOpção: ";
		cin>>opc;
		switch(opc){
			case 1:
				cout<<"\nNome do arquivo de entrada: ";
				cin>>nome_entrada;
				cout<<"\nNome do arquivo de saída: ";
				cin>>nome_saida;
				cout<<"\nConvertendo ...\n\n";
				system (("jupyter nbconvert --to html " + nome_entrada +".ipynb").c_str());
				system (("pandoc -s " + nome_entrada + ".html -o " + nome_saida + ".docx").c_str());
				system (("wkhtmltopdf "  + nome_entrada + ".html "  + nome_saida + ".pdf").c_str());
		
				system (("rm "+ nome_entrada +".html" ).c_str());
				break;
			case 2:
				cout<<"\nNome do arquivo de entrada: ";
				cin>>nome_entrada;
				cout<<"\nConvertendo ...\n\n";
				system (("jupyter nbconvert --to script " + nome_entrada +".ipynb").c_str());
				break;
				
			case 0:
				return 0;
				break;
				
			default:
				cout<<"\n[1] De jupyter para PDF\n[2] De jupyter para script\nOpção][\b\b";
				cin>>opc;
				break;
		}
	}while (opc!=0);
	
}
