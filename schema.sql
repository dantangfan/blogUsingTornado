/*init sql*/

drop database if exists website;

create database website;

use website;


create table article(
    id integer primary key auto_increment,
    title char(40) not null,
    publish_time datetime not null,
    summary text not null,
    content text not null
)engine=innodb default charset=utf8;


create table comment(
    id int primary key auto_increment,
    article_id int not null,
    user_name text not null,
    user_email text not null,
    website text,
    create_at datetime not null,
    content text not null,
    to_comment_id int not null
)engine=innodb default charset=utf8;


create table timeline(
    id int primary key auto_increment,
    time datetime not null,
    content text not null,
    user_name text not null,
    user_email text not null
)engine=innodb default charset=utf8;