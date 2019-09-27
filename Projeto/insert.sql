-- Passo 1: selecionar o banco de dados
use projetofuncionarios;

-- Passo 2: script para criar uma tabela

CREATE TABLE funcionarios_dados (
    id_func int not null auto_increment,
    nome_func varchar(50) not null,
    cpf_func int (20) not null,
    idade_func int not null,
    PRIMARY KEY (id_func)
);
