

insert into user values
(1,"mary@example.com", "Mary", "pwd"),
(2,"ana@example.com", "Ana", "pwd");

insert into movie VALUES
(11, "Movie1", "Director1", NULL, "https://hips.hearstapps.com/es.h-cdn.co/fotoes/images/media/imagenes/recursos/blade-runner-poster/136792680-1-esl-ES/blade-runner-poster.jpg?resize=480:*"),
(22, "Movie2", "Director1", "Art", "https://ih1.redbubble.net/image.266694672.1531/flat,750x,075,f-pad,750x1000,f8f8f8.u2.jpg"),
(33, "Movie3", "Director2", "Drama", "https://image.posterlounge.es/images/l/1898959.jpg");

insert into screen VALUES
(91, "H1", 30),
(81, "H2", 24),
(71, "H3", 40);

insert into projection VALUES
(111, CURRENT_TIMESTAMP, 11, 91),
(222, CURRENT_TIMESTAMP, 22, 81),
(333, CURRENT_TIMESTAMP, 33, 71);


