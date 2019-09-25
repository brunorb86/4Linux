-- Select
use 4linux;

SELECT * FROM pessoa;

SELECT * FROM pessoa
WHERE nac_pessoa = 'Brasileira';

SELECT * FROM pessoa
WHERE idade_pessoa > 40;

SELECT * FROM pessoa
WHERE nome_pessoa like 'Bru%';
