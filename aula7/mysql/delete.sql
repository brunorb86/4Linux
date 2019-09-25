-- DELETE

USE 4linux;

SELECT * FROM pessoa;

DELETE FROM pessoa
WHERE nac_pessoa = "Brasileira";

SELECT * FROM pessoa;
