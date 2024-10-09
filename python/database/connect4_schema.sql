DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player;

CREATE TABLE Player (
    P_ID    CHAR(18),
    P_Win   NUMBER,
    P_Lose  NUMBER,
    P_Draw  NUMBER,

    CONSTRAINT PlayerPK PRIMARY KEY(P_ID)
);

CREATE TABLE Match (
    M_ID                NUMBER,
    M_RedPlayerID       CHAR(18),
    M_YellowPlayerID    CHAR(18),
    M_Sequence          VARCHAR(42),
    M_WinPlayer         CHAR(1),
    M_Date              DATE, 

    CONSTRAINT MatchPK PRIMARY KEY(M_ID),
    CONSTRAINT M_RedPlayerFK FOREIGN KEY(M_RedPlayerID) REFERENCES Player(P_ID),
    CONSTRAINT M_YellowPlayerFK FOREIGN KEY(M_YellowPlayerID) REFERENCES Player(P_ID)
);
