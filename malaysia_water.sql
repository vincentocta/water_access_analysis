SELECT 
    state,
    ROUND(AVG(proportion), 2) AS avg_access,
    ROUND(MIN(proportion), 2) AS min_access,
    ROUND(MAX(proportion), 2) AS max_access
FROM water_access
WHERE strata = 'overall'
AND state != 'Malaysia'
GROUP BY state
ORDER BY avg_access ASC;

SELECT 
    strftime('%Y', date) AS year,
    SUM(water_production) AS total_production,
    (SELECT SUM(wc.water_consumption) 
     FROM water_consumption wc 
     WHERE strftime('%Y', wc.date) = strftime('%Y', wp.date)) AS total_consumption,
    SUM(water_production) - 
    (SELECT SUM(wc.water_consumption) 
     FROM water_consumption wc 
     WHERE strftime('%Y', wc.date) = strftime('%Y', wp.date)) AS gap,
    ROUND(
    (SELECT SUM(wc.water_consumption) 
     FROM water_consumption wc 
     WHERE strftime('%Y', wc.date) = strftime('%Y', wp.date)) * 100.0 
     / SUM(water_production), 2) AS consumption_per_production
FROM water_production wp
GROUP BY year
ORDER BY year ASC;

SELECT 
    strftime('%Y', date) AS year,
    ROUND(AVG(proportion), 2) AS national_access,
    ROUND(AVG(proportion) - LAG(AVG(proportion)) 
        OVER (ORDER BY strftime('%Y', date)), 2) AS year_on_year
FROM water_access
WHERE state = 'Malaysia'
AND strata = 'overall'
GROUP BY year
ORDER BY year ASC;

-- 2006: -0.2 early reform disruption
-- 2007: -4.3 peak reform fallout  
-- 2016: -0.2 early infrastructure decay
-- 2019: -0.4 Sabah crisis begins
-- 2020: -0.7 Sabah collapse + COVID impact

SELECT 
    strftime('%Y', date) AS year,
    ROUND(SUM(CASE WHEN sector = 'domestic' 
        THEN water_consumption ELSE 0 END), 2) AS domestic_consumption,
    ROUND(SUM(CASE WHEN sector = 'nondomestic' 
        THEN water_consumption ELSE 0 END), 2) AS non_domestic_consumption,
    ROUND(SUM(CASE WHEN sector = 'domestic' 
        THEN water_consumption ELSE 0 END) * 100.0 
        / SUM(water_consumption), 2) AS domestic_percentage,
    ROUND(SUM(CASE WHEN sector = 'nondomestic' 
        THEN water_consumption ELSE 0 END) * 100.0 
        / SUM(water_consumption), 2) AS non_domestic_percentage
FROM water_consumption
GROUP BY year
ORDER BY year ASC;

SELECT 
    state,
    ROUND(AVG(proportion), 2) AS avg_access,
    ROUND(AVG(proportion) - (
        SELECT AVG(proportion) 
        FROM water_access 
        WHERE state = 'Malaysia' 
        AND strata = 'overall'
    ), 2) AS gap_from_national_avg
FROM water_access
WHERE strata = 'overall'
AND state != 'Malaysia'
GROUP BY state
HAVING AVG(proportion) < (
    SELECT AVG(proportion) 
    FROM water_access 
    WHERE state = 'Malaysia' 
    AND strata = 'overall'
)
ORDER BY avg_access ASC;

SELECT 
    state,
    ROUND(AVG(CASE WHEN strata = 'urban' 
        THEN proportion END), 2) AS avg_urban_access,
    ROUND(AVG(CASE WHEN strata = 'rural' 
        THEN proportion END), 2) AS avg_rural_access,
    ROUND(AVG(CASE WHEN strata = 'urban' 
        THEN proportion END) - 
    AVG(CASE WHEN strata = 'rural' 
        THEN proportion END), 2) AS urban_rural_gap
FROM water_access
WHERE state != 'Malaysia'
GROUP BY state
ORDER BY urban_rural_gap DESC;

-- Sabah: 33% urban-rural gap — largest in Malaysia
-- Water exists in cities, rural communities are bypassed entirely
-- Distribution failure, not supply failure