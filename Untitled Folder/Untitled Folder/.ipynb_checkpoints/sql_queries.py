DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS CENTROS(
NUMCE	INT PRIMARY KEY,
NOMCE	VARCHAR(25),
DIRCE	 VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS EMPLEADOS(
NUMEM	INT PRIMARY KEY,
EXTEL	INT,
FECNA	DATE,
FECIN	DATE,
SALAR	DECIMAL(7,2),
COMIS	DECIMAL(5,2),
NUMHI	INT,
NOMEM	VARCHAR(10),
NUMDE	INT
);

CREATE TABLE IF NOT EXISTS DEPARTAMENTOS (
    NUMDE	INT PRIMARY KEY,
    NUMCE	INT,
    DIREC	INT,
    TIDIR	CHAR(1),
    PRESU	DECIMAL(3,1),
    DEPDE	INT,
    NOMDE	VARCHAR(20),
    CONSTRAINT fk_centro_departamento
        FOREIGN KEY (NUMCE)
        REFERENCES CENTROS(NUMCE),
    CONSTRAINT fk_empleado_departamento
        FOREIGN KEY (NUMDE)
        REFERENCES EMPLEADOS(NUMDE)
);
'''