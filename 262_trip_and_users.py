# Write your MySQL query statement below

SELECT Request_at Day, ROUND(COUNT(Status <> 'completed' OR NULL)/COUNT(*),2) `Cancellation Rate` from Users INNER JOIN Trips  on Users_Id = Client_Id AND Banned = 'No' AND  Request_at BETWEEN '2013-10-01' AND '2013-10-03' GROUP By Request_at


SELECT Request_at Day, ROUND(SUM(CASE WHEN STATUS LIKE 'cancelled_%' THEN 1 ELSE 0 END)/COUNT(*),2) `Cancellation Rate` from Users INNER JOIN Trips  on Users_Id = Client_Id AND Banned = 'No' AND  Request_at BETWEEN '2013-10-01' AND '2013-10-03' GROUP By Request_at

