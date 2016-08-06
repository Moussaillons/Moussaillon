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
    pass_hash text not null,
    site integer REFERENCES sites(id)
);

drop table if exists sessions;
create table sessions (
    id integer primary key autoincrement,
    creation datetime not null,
    member integer REFERENCES members(id)
);
