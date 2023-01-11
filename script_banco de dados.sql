create schema fiotech_email;

CREATE TABLE `fiotech_email`.`arquivo_email` (
  `nome_arquivo` VARCHAR(255) NOT NULL,
  `remetente` VARCHAR(255) NOT NULL,
  `destinatario` VARCHAR(255) NOT NULL,
  `data_hora` VARCHAR(255) NOT NULL,
  `conteudo` TEXT NOT NULL,
  PRIMARY KEY (`nome_arquivo`));
  
  CREATE TABLE `fiotech_email`.`palavra_chave` (
  `chave` VARCHAR(255) NOT NULL,
  `tipo` VARCHAR(255) NOT NULL);
  

