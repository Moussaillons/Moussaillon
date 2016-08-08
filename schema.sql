drop table if exists sites;
create table sites (
    id integer primary key autoincrement,
    uri text not null,
    name text not null,
    description text
);

INSERT into sites(uri, name) VALUES ('', 'Moussaillon');

drop table if exists members;
create table members (
    id integer primary key autoincrement,
    mail text not null,
    name text not null,
    password text not null,
    site integer REFERENCES sites(id)
);

INSERT into members(mail, name, password, site) VALUES ('hello@domain.dev', 'John Anglin', '$2a$12$WZKyAa1hdAUoww5WU1RXIOuo9bfDFsz82fzw5/bXpPcwDmgmKNoSe', '');

drop table if exists sessions;
create table sessions (
    key text primary key,
    last_ping datetime not null,
    member integer REFERENCES members(id)
);
