DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player;

CREATE TABLE Player (
    P_ID    TEXT,
    P_Win   INTEGER,
    P_Lose  INTEGER,
    P_Draw  INTEGER,

    PRIMARY KEY(P_ID)
);

CREATE TABLE Match (
    M_ID                INTEGER,
    M_RedPlayerID       TEXT,
    M_YellowPlayerID    TEXT,
    M_Sequence          TEXT,
    M_WinPlayer         TEXT,
    M_Date              TEXT, 

    PRIMARY KEY(M_ID),
    FOREIGN KEY(M_RedPlayerID) REFERENCES Player(P_ID),
    FOREIGN KEY(M_YellowPlayerID) REFERENCES Player(P_ID)
);
