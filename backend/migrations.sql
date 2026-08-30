DROP TABLE IF EXISTS games;

CREATE TABLE games(  
    id TEXT PRIMARY KEY,
    name TEXT,
    publisher TEXT,
    developer TEXT,
    keywords TEXT,
    release_date TEXT,
    avg_time REAL,
    platforms TEXT,
    created_at TEXT,
    updated_at TEXT,
    deleted_at TEXT
);

DROP TABLE IF EXISTS users;

CREATE TABLE users(  
    id TEXT PRIMARY KEY,
    name TEXT,
    nickname TEXT,
    birthdate TEXT,
    interests TEXT,
    created_at TEXT,
    updated_at TEXT,
    deleted_at TEXT
);

DROP TABLE IF EXISTS users_games;

CREATE TABLE users_games (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    game_id TEXT NOT NULL,
    status INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    recommended_by TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    deleted_at TEXT,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (game_id) REFERENCES games(id),

    UNIQUE (user_id, game_id)
);

DROP TABLE IF EXISTS keywords;

CREATE TABLE keywords (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    deleted_at TEXT,

    UNIQUE (name)
);

DROP TABLE IF EXISTS games_keywords;

CREATE TABLE games_keywords (
    id TEXT PRIMARY KEY,
    keyword_id TEXT NOT NULL,
    game_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    deleted_at TEXT,

    FOREIGN KEY (keyword_id) REFERENCES keywords(id),
    FOREIGN KEY (game_id) REFERENCES games(id),

    UNIQUE (keyword_id, game_id)
);