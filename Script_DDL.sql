CREATE DATABASE TournamentApp;
go

USE TournamentApp;
go


CREATE TABLE director_tecnico (
    id INT PRIMARY KEY,
    nombre NVARCHAR(255) NOT NULL,
    nacionalidad NVARCHAR(255) NOT NULL,
    porcentaje FLOAT NOT NULL
);


CREATE TABLE equipo (
    id INT PRIMARY KEY,
    logotipo NVARCHAR(MAX) NOT NULL,
    nombre NVARCHAR(255) NOT NULL,
    director_tecnico_id INT,
    FOREIGN KEY (director_tecnico_id) REFERENCES director_tecnico(id)
);


CREATE TABLE torneo (
    id INT PRIMARY KEY,
    fecha NVARCHAR(255) NOT NULL,
    nombre NVARCHAR(255) NOT NULL
);


CREATE TABLE partido (
    id INT PRIMARY KEY,
    torneo_id INT,
    equipo1_id INT,
    equipo2_id INT,
    estadio NVARCHAR(255) NOT NULL,
    fecha DATETIME NOT NULL,
    FOREIGN KEY (torneo_id) REFERENCES torneo(id),
    FOREIGN KEY (equipo1_id) REFERENCES equipo(id),
    FOREIGN KEY (equipo2_id) REFERENCES equipo(id)
);


CREATE TABLE jugador (
    id INT PRIMARY KEY,
    equipo_id INT,
    nombre NVARCHAR(255) NOT NULL,
    numero INT NOT NULL,
    nacionalidad NVARCHAR(255) NOT NULL,
    posicion NVARCHAR(255) NOT NULL,
    rol NVARCHAR(255) NOT NULL,
    FOREIGN KEY (equipo_id) REFERENCES equipo(id)
);


CREATE TABLE equipo_torneo (
    id INT PRIMARY KEY,
    torneo_id INT,
    equipo_id INT,
    goles INT NOT NULL,
    puntos INT NOT NULL,
    partidos_ganados INT NOT NULL,
    partidos_empatados INT NOT NULL,
    partidos_perdidos INT NOT NULL,
    FOREIGN KEY (torneo_id) REFERENCES torneo(id),
    FOREIGN KEY (equipo_id) REFERENCES equipo(id)
);


CREATE TABLE posiciones (
    id INT PRIMARY KEY,
    torneo_id INT,
    FOREIGN KEY (torneo_id) REFERENCES torneo(id)
);


CREATE TABLE resultado (
    id INT PRIMARY KEY,
    partido_id INT,
    goles_equipo1 INT NOT NULL,
    goles_equipo2 INT NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partido(id)
);


CREATE TABLE partido_resultado (
    id INT PRIMARY KEY,
    torneo INT,
    equipo1 INT,
    equipo2 INT,
    estadio NVARCHAR(255) NOT NULL,
    fecha DATETIME NOT NULL,
    resultado INT,
    FOREIGN KEY (torneo) REFERENCES torneo(id),
    FOREIGN KEY (equipo1) REFERENCES equipo(id),
    FOREIGN KEY (equipo2) REFERENCES equipo(id)
);


CREATE TABLE tabla_posiciones_equipo_torneo (
    id INT PRIMARY KEY,
    tabla_posiciones_id INT,
    equipo_torneo_id INT,
    FOREIGN KEY (tabla_posiciones_id) REFERENCES posiciones(id),
    FOREIGN KEY (equipo_torneo_id) REFERENCES equipo_torneo(id)
);
