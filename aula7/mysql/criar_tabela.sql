-- Passo 1: selecionar o banco de dados
use 4linux;

-- Passo 2: script para criar uma tabela

CREATE TABLE pessoa (
    id_pessoa int not null auto_increment,
    nome_pessoa varchar(50) not null,
    nac_pessoa varchar (20) not null,
    idade_pessoa int not null,
    PRIMARY KEY (id_pessoa)
);
