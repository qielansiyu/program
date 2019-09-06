SELECT Id,count(Category='hotel') AS HotelOrdCnt,
    count(Category='flight') AS FlightOrdCnt,
    avg(Amount) AS AvgAmount
FROM Detail
GROUP BY Id
HAVING OrderDate LIKE "2019%"
ORDER BY Id

create table Detail (Id BIGINT, OrderDate STRING, Category STRING, Amount DOUBLE);
insert into Detail(Id, OrderDate, Category, Amount) values(1001, '2018-06-01', 'hotel', 300.0);
insert into Detail(Id, OrderDate, Category, Amount) values(1001, '2019-03-01', 'flight', 1000.0);
insert into Detail(Id, OrderDate, Category, Amount) values(1001, '2019-03-01', 'hotel', 450.0);
insert into Detail(Id, OrderDate, Category, Amount) values(1002, '2019-01-01', 'flight', 850.0);
insert into Detail(Id, OrderDate, Category, Amount) values(1002, '2019-01-03', 'flight', 750.0);
insert into Detail(Id, OrderDate, Category, Amount) values(1002, '2019-05-03', 'hotel', 500.0);