--Usuario(ID,Nome)
--Equipamento(ID,Nome,Status,Limite_Temp_Empr,Disponibilidade,Data_ultima_revis,Numero_patrimonio,Descricao) Categoria -> Categoria
--Emprestimo(ID,Data_Emprestimo,Nota,Nome_Usuario,ID_Equipamento,Comentario,Dava_Devolucao,Hora_Emprestimo,Hora_Devolucao,Data_Devolucao_Prevista) Nome_Usuario -> Usuario; ID_Equipamento -> Equipamento
--Sala(Nome,ID_Armario) ID_Armario -> Armario
--Armario(ID,ID_Caixa,Nome) ID_Caixa -> Caixa
--Caixa(ID,ID_Equipamento,Descricao) ID_Equipamento -> Equipamento
--Categoria(ID,Nome,Superior) Superior -> Categoria

DROP TABLE Usuario;
CREATE TABLE Usuario(
	ID SERIAL PRIMARY KEY,
	Nome VARCHAR(255) NOT NULL
);

CREATE TABLE Categoria(
	ID SERIAL PRIMARY KEY,
	Nome VARCHAR NOT NULL,
	Superior VARCHAR,
	FOREIGN KEY (Superior) REFERENCES Categoria(Nome)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
);

CREATE TABLE Equipamento(
	ID SERIAL PRIMARY KEY,
	Nome VARCHAR(255) NOT NULL,
	Status VARCHAR(255) NOT NULL,
	Limite_Temp_Empr DATE,
	Disponibilidade VARCHAR(255) NOT NULL,
	Data_ultima_revis DATE,
	Numero_patrimonio INT,
	Descricao VARCHAR,
	Categoria varchar(255),
	FOREIGN KEY (Categoria) REFERENCES Categoria(Nome)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION

);

CREATE TABLE Emprestimo(
	ID SERIAL NOT NULL,
	Nome_Usuario VARCHAR(255) NOT NULL,
	ID_Equipamento SERIAL NOT NULL,
	Nota INT,
	Comentario VARCHAR,
	Data_Emprestimo DATE NOT NULL,
	Dava_Devolucao DATE,
	Data_Devolucao_Prevista DATE NOT NULL,
	Hora_Emprestimo TIME NOT NULL,
	Hora_Devolucao TIME,
	PRIMARY KEY (ID,Nome_Usuario,ID_Equipamento,Data_Emprestimo),
	FOREIGN KEY (Nome_Usuario) REFERENCES Usuario(Nome)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	FOREIGN KEY (ID_Equipamento) REFERENCES Equipamento(ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
);

CREATE TABLE Caixa(
	ID SERIAL NOT NULL,
	Numero INT,
	PRIMARY key (ID)
);

CREATE TABLE Armario(
	ID SERIAL NOT NULL,
	Nome VARCHAR,
	ID_Caixa INT NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (ID_Caixa) REFERENCES Caixa(ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION

);

CREATE TABLE Sala(
	ID SERIAL NOT NULL,
	Nome VARCHAR NOT NULL
	ID_Armario INT NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (ID_Armario) REFERENCES Armario(ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION
);