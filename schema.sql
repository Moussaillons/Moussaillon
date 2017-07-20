drop table if exists sites;
create table sites (
    id integer primary key autoincrement,
    uri text not null,
    name text not null,
    description text
);

INSERT into sites(uri, name, description) VALUES ('', 'Fédération UCP', 'Fédération des associations de l UCP');
INSERT into sites(uri, name, description) VALUES ('echo', '>Echo', 'Association des cultures électronique de l UCP');
INSERT into sites(uri, name, description) VALUES ('hazybot', 'Hazybot', 'Association de robotique de l UCP');

drop table if exists members;
create table members (
    id integer primary key autoincrement,
    mail text not null,
    name text not null,
    password text not null
);

-- Every password is Potatoes14
INSERT into members(mail, name, password) VALUES ('louis@domain.dev', 'Louis Desportes', 'pbkdf2:sha256:50000$BiZ6XJub$d82d74df2e3477365da24142a4af19f3ad282723c53e5c4f7e6a9bcd0980d79d');
INSERT into members(mail, name, password) VALUES ('alex@domain.dev', 'Alexandre Fourgs', 'pbkdf2:sha256:50000$BiZ6XJub$d82d74df2e3477365da24142a4af19f3ad282723c53e5c4f7e6a9bcd0980d79d');
INSERT into members(mail, name, password) VALUES ('bastien@domain.dev', 'Bastien Lepesant', 'pbkdf2:sha256:50000$BiZ6XJub$d82d74df2e3477365da24142a4af19f3ad282723c53e5c4f7e6a9bcd0980d79d');

drop table if exists is_member;
create table is_member (
    id integer primary key autoincrement,
    person integer REFERENCES members(id),
    site integer REFERENCES sites(id)
);

INSERT INTO is_member(person, site) VALUES (0, 0);
INSERT INTO is_member(person, site) VALUES (0, 1);
INSERT INTO is_member(person, site) VALUES (1, 1);
INSERT INTO is_member(person, site) VALUES (2, 2);

drop table if exists sessions;
create table sessions (
    key text primary key,
    last_ping datetime not null,
    member integer REFERENCES members(id)
);

drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    site integer REFERENCES sites(id),
    URI text not null,
    title text not null,
    content text not null,
    publication datetime not null
);

INSERT into posts(site, URI, title, content, publication) VALUES (1, 'merci', 'Merci mon capitaine!', "Merci de m'avoir accepté en tant que mousse mon capitaine. Je ne vous décevrai pas!", 'now');
