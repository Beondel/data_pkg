-- Populate second test set with non-extreme count mhc's
INSERT INTO mhc_test2
SELECT *
FROM mhc_data
WHERE mhc in (SELECT mhc
              FROM data
              GROUP BY mhc
              HAVING COUNT(*) > 10 and COUNT(*) < 3000);

-- Remove all but 12 groups
DELETE
FROM mhc_test2
WHERE mhc NOT IN (SELECT mhc
                  FROM mhc_test2
                  GROUP BY mhc
                  ORDER BY random()
                  LIMIT 12);

-- Populate training set with mhc's not in the second testing set
INSERT INTO mhc_train
SELECT *
FROM mhc_data x
WHERE x.mhc NOT IN (SELECT DISTINCT mhc
                    FROM mhc_test2);


-- Purge Train set of any tuples in test set 1
DELETE
FROM mhc_train
WHERE id IN (SELECT y.id
             FROM mhc_test1 AS y);