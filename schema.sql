--init sql

drop database if exists website;

create website;

use website;


create table article(
    'id' integer primary key auto_increment,
    'title' text not null,
    'publish_time' date not null,
    'summary' text not null,
    'content' mediumtext not null
)engine=innodb default charset=utf8;


create comment(
    'id' integer primary key auto_increment,
    'article_id' integer not null,
    'user_name' text not null,
    'user_email' text not null,
    'website' text,
    'create_at' date not null,
    'content' text not null,
    'to_comment_id' integer not null
)engine=innodb default charset=utf8;


