use dataanalytics_db;
select * from metalminerals;
#First Moment Business Decision / Measures of Central Tendency#

# Mean For All Columns

SELECT 
AVG(Price_Aluminium_per_Ton) AS mean_Price_Aluminium_per_Ton, # Mean = '2518.154'
AVG(Price_Tin_per_Ounce) AS mean_Price_Tin_per_Ounce, # Mean = '2502.216'
AVG(Price_Copper_per_Ton) AS mean_Price_Copper_per_Ton, # Mean = '2504.965'
AVG(Price_Iron_per_Ounce) AS mean_Price_Iron_per_Ounce, # Mean = '2533.410'
AVG(Price_Steel_per_Ton) AS mean_Price_Steel_per_Ton, # Mean = '2534.986'
AVG(Inflation_Rate_Percentage) AS mean_Inflation_Rate_Percentage, # Mean = '2489.164'
AVG(Aluminium_Price_Inflation_Adjusted) AS mean_Aluminium_Price_Inflation_Adjusted, # Mean = '2438.135'
AVG(Tin_Price_Inflation_Adjusted) AS mean_Tin_Price_Inflation_Adjusted, # Mean = '2477.110'
AVG(Copper_Price_Inflation_Adjusted) AS mean_Copper_Price_Inflation_Adjusted, # Mean = '2626.288'
AVG(Iron_Price_Inflation_Adjusted) AS mean_Iron_Price_Inflation_Adjusted, # Mean = '2569.264'
AVG(Steel_Price_Inflation_Adjusted) AS mean_Steel_Price_Inflation_Adjusted, # Mean = '2434.056'
AVG(Price_Chromium_Adjusted) AS mean_Price_Chromium_Adjusted # Mean = '2469.829'
FROM metalminerals;

# Median for all columns
SELECT 
Price_Aluminium_per_Ton AS median_Price_Aluminium_per_Ton, # Median = '2401.76'
Price_Tin_per_Ounce AS median_Price_Tin_per_Ounce, # Median = '2973.81'
Price_Copper_per_Ton AS median_Price_Copper_per_Ton, # Median = '340.3'
Price_Iron_per_Ounce AS median_Price_Iron_per_Ounce, # Median = '1832.41'
Price_Steel_per_Ton AS median_Price_Steel_per_Ton, # Median = '2072.91'
Inflation_Rate_Percentage AS median_Inflation_Rate_Percentage, # Median = '3150.52'
Aluminium_Price_Inflation_Adjusted AS median_Aluminium_Price_Inflation_Adjusted, # Median = '4005.73'
Tin_Price_Inflation_Adjusted AS median_Tin_Price_Inflation_Adjusted, # Median = '1698.22'
Copper_Price_Inflation_Adjusted AS median_Copper_Price_Inflation_Adjusted, # Median = '2260.65'
Iron_Price_Inflation_Adjusted AS median_Iron_Price_Inflation_Adjusted, # Median = '4000.09'
Steel_Price_Inflation_Adjusted AS median_Steel_Price_Inflation_Adjusted, # Median = '2470.94'
Price_Chromium_Adjusted AS median_Price_Chromium_Adjusted # Median = '976.9'
FROM (
SELECT 
Price_Aluminium_per_Ton, ROW_NUMBER() OVER (ORDER BY Price_Aluminium_per_Ton) AS row_num,
Price_Tin_per_Ounce, ROW_NUMBER() OVER (ORDER BY Price_Tin_per_Ounce) ,
Price_Copper_per_Ton, ROW_NUMBER() OVER (ORDER BY Price_Copper_per_Ton) ,
Price_Iron_per_Ounce, ROW_NUMBER() OVER (ORDER BY Price_Iron_per_Ounce) ,
Price_Steel_per_Ton, ROW_NUMBER() OVER (ORDER BY Price_Steel_per_Ton)  ,
Inflation_Rate_Percentage, ROW_NUMBER() OVER (ORDER BY Inflation_Rate_Percentage) ,
Aluminium_Price_Inflation_Adjusted, ROW_NUMBER() OVER (ORDER BY Aluminium_Price_Inflation_Adjusted) ,
Tin_Price_Inflation_Adjusted, ROW_NUMBER() OVER (ORDER BY Tin_Price_Inflation_Adjusted) ,
Copper_Price_Inflation_Adjusted, ROW_NUMBER() OVER (ORDER BY Copper_Price_Inflation_Adjusted) ,
Iron_Price_Inflation_Adjusted, ROW_NUMBER() OVER (ORDER BY Iron_Price_Inflation_Adjusted) ,
Steel_Price_Inflation_Adjusted, ROW_NUMBER() OVER (ORDER BY Steel_Price_Inflation_Adjusted) ,
Price_Chromium_Adjusted, ROW_NUMBER() OVER (ORDER BY Price_Chromium_Adjusted) ,
COUNT(*) OVER () AS total_count
FROM metalminerals
) AS subquery
WHERE row_num = (total_count + 1) / 2 OR row_num = (total_count + 2) / 2;

# Mode of all Columns
SELECT 
AVG(Price_Aluminium_per_Ton) AS mean_Price_Aluminium_per_Ton, #Mode = '3475.63'
AVG(Price_Tin_per_Ounce) AS mean_Price_Tin_per_Ounce, #Mode = '3293.28'
AVG(Price_Copper_per_Ton) AS mean_Price_Copper_per_Ton, #Mode = Null
AVG(Price_Iron_per_Ounce) AS mean_Price_Iron_per_Ounce, #Mode = '2592.76'
AVG(Price_Steel_per_Ton) AS mean_Price_Steel_per_Ton, #Mode = '2049.01'
AVG(Inflation_Rate_Percentage) AS mean_Inflation_Rate_Percentage, #Mode = '2071.55'
AVG(Aluminium_Price_Inflation_Adjusted) AS mean_Aluminium_Price_Inflation_Adjusted, #Mode = '4443.15'
AVG(Tin_Price_Inflation_Adjusted) AS mean_Tin_Price_Inflation_Adjusted, #Mode = '4211.52'
AVG(Copper_Price_Inflation_Adjusted) AS mean_Copper_Price_Inflation_Adjusted, #Mode = '3008.46'
AVG(Iron_Price_Inflation_Adjusted) AS mean_Iron_Price_Inflation_Adjusted, #Mode = '1400.33'
AVG(Steel_Price_Inflation_Adjusted) AS mean_Steel_Price_Inflation_Adjusted, #Mode = '341.31'
AVG(Price_Chromium_Adjusted) AS mean_Price_Chromium_Adjusted #Mode = '1282.84'
FROM metalminerals;
SELECT 
Price_Aluminium_per_Ton AS mode_Price_Aluminium_per_Ton,
Price_Tin_per_Ounce AS mode_Price_Tin_per_Ounce,
Price_Copper_per_Ton AS mode_Price_Copper_per_Ton,
Price_Iron_per_Ounce AS mode_Price_Iron_per_Ounce,
Price_Steel_per_Ton AS mode_Price_Steel_per_Ton,
Inflation_Rate_Percentage AS mode_Inflation_Rate_Percentage,
Aluminium_Price_Inflation_Adjusted AS mode_Aluminium_Price_Inflation_Adjusted,
Tin_Price_Inflation_Adjusted AS mode_Tin_Price_Inflation_Adjusted,
Copper_Price_Inflation_Adjusted AS mode_Copper_Price_Inflation_Adjusted,
Iron_Price_Inflation_Adjusted AS mode_Iron_Price_Inflation_Adjusted,
Steel_Price_Inflation_Adjusted AS mode_Steel_Price_Inflation_Adjusted,
Price_Chromium_Adjusted AS mode_Price_Chromium_Adjusted
FROM (
SELECT 
Price_Aluminium_per_Ton, COUNT(*) AS frequency,
Price_Tin_per_Ounce,
Price_Copper_per_Ton, 
Price_Iron_per_Ounce,
Price_Steel_per_Ton, 
Inflation_Rate_Percentage,
Aluminium_Price_Inflation_Adjusted, 
Tin_Price_Inflation_Adjusted, 
Copper_Price_Inflation_Adjusted, 
Iron_Price_Inflation_Adjusted, 
Steel_Price_Inflation_Adjusted, 
Price_Chromium_Adjusted 
FROM metalminerals
GROUP BY
 Price_Aluminium_per_Ton, 
Price_Tin_per_Ounce,
Price_Copper_per_Ton, 
Price_Iron_per_Ounce,
Price_Steel_per_Ton, 
Inflation_Rate_Percentage,
Aluminium_Price_Inflation_Adjusted, 
Tin_Price_Inflation_Adjusted, 
Copper_Price_Inflation_Adjusted, 
Iron_Price_Inflation_Adjusted, 
Steel_Price_Inflation_Adjusted, 
Price_Chromium_Adjusted 
ORDER BY frequency DESC
LIMIT 1
) AS subquery;


#Second Moment Business Decision / Measures of Dispersion#

#Standard Deviation#
SELECT 
STDDEV( Price_Aluminium_per_Ton ) AS  Price_Aluminium_per_Ton_stddev, #Stddev ='1449.576'
STDDEV(Price_Tin_per_Ounce) AS Price_Tin_per_Ounce_stddev,  #Stddev ='1445.825'
STDDEV(Price_Copper_per_Ton ) AS Price_Copper_per_Ton_stddev,  #Stddev ='1437.195'
STDDEV(Price_Iron_per_Ounce) AS Price_Iron_per_Ounce_stddev,  #Stddev ='1433.993'
STDDEV(Price_Steel_per_Ton) AS Price_Steel_per_Ton_stddev,  #Stddev ='1418.114'
STDDEV(Inflation_Rate_Percentage) AS Inflation_Rate_Percentage_stddev,  #Stddev ='1440.220'
STDDEV(Aluminium_Price_Inflation_Adjusted) AS Aluminium_Price_Inflation_Adjusted_stddev,  #Stddev ='1399.619'
STDDEV(Tin_Price_Inflation_Adjusted) AS Tin_Price_Inflation_Adjusted_stddev,  #Stddev ='1406.309'
STDDEV(Copper_Price_Inflation_Adjusted) AS Copper_Price_Inflation_Adjusted_stddev,  #Stddev ='2708.948'
STDDEV(Iron_Price_Inflation_Adjusted) AS Iron_Price_Inflation_Adjusted_stddev,  #Stddev ='1442.701'
STDDEV(Steel_Price_Inflation_Adjusted) AS Steel_Price_Inflation_Adjusted_stddev,  #Stddev ='1421.755'
STDDEV(Price_Chromium_Adjusted) AS Price_Chromium_Adjusted_stddev  #Stddev ='1446.751'
FROM metalminerals;

#Range#
SELECT 
MAX(Price_Aluminium_per_Ton) - MIN(Price_Aluminium_per_Ton) AS Price_Aluminium_per_Ton_range, #Range = '4983.3'
MAX(Price_Tin_per_Ounce) - MIN(Price_Tin_per_Ounce) AS Price_Tin_per_Ounce_range, #Range = 4983.03
MAX(Price_Copper_per_Ton) - MIN(Price_Copper_per_Ton) AS Price_Copper_per_Ton_range, #Range =  4967.54
MAX(Price_Iron_per_Ounce) - MIN(Price_Iron_per_Ounce) AS Price_Iron_per_Ounce_range, #Range = 4958.65
MAX(Price_Steel_per_Ton) - MIN(Price_Steel_per_Ton) AS Price_Steel_per_Ton_range, #Range = 4982.45
MAX(Inflation_Rate_Percentage) - MIN(Inflation_Rate_Percentage) AS Inflation_Rate_Percentage_range, #Range = 4965.16
MAX(Aluminium_Price_Inflation_Adjusted) - MIN(Aluminium_Price_Inflation_Adjusted) AS Aluminium_Price_Inflation_Adjusted_range, #Range = 4968.400
MAX(Tin_Price_Inflation_Adjusted) - MIN(Tin_Price_Inflation_Adjusted) AS Tin_Price_Inflation_Adjusted_range, #Range = 4960.559
MAX(Copper_Price_Inflation_Adjusted) - MIN(Copper_Price_Inflation_Adjusted) AS Copper_Price_Inflation_Adjusted_range, #Range =  43562.817
MAX(Iron_Price_Inflation_Adjusted) - MIN(Iron_Price_Inflation_Adjusted) AS Iron_Price_Inflation_Adjusted_range, #Range = 4967.610
MAX(Steel_Price_Inflation_Adjusted) - MIN(Steel_Price_Inflation_Adjusted) AS Steel_Price_Inflation_Adjusted_range, #Range = 4976.389
MAX(Price_Chromium_Adjusted) - MIN(Price_Chromium_Adjusted) AS Price_Chromium_Adjusted_range #Range = 4984.88
FROM metalminerals;

#Variance#
SELECT 
VARIANCE(Price_Aluminium_per_Ton) AS Price_Aluminium_per_Ton_variance, #Varaince = '2101270.948574901'
VARIANCE(Price_Tin_per_Ounce) AS Price_Tin_per_Ounce_variance, #Varaince = '2090411.5918314348'
VARIANCE(Price_Copper_per_Ton) AS Price_Copper_per_Ton_variance, #Varaince = '2065531.1771433547'
VARIANCE(Price_Iron_per_Ounce) AS Price_Iron_per_Ounce_variance, #Varaince = '2056338.493612616'
VARIANCE(Price_Steel_per_Ton) AS Price_Steel_per_Ton_variance, #Varaince = '2011049.3763826909'
VARIANCE(Inflation_Rate_Percentage) AS Inflation_Rate_Percentage_variance, #Varaince = '2074236.354663932'
VARIANCE(Aluminium_Price_Inflation_Adjusted) AS Aluminium_Price_Inflation_Adjusted_variance, #Varaince = '1958934.5963776454'
VARIANCE(Tin_Price_Inflation_Adjusted) AS Tin_Price_Inflation_Adjusted_variance, #Varaince = '1977706.8770085901'
VARIANCE(Copper_Price_Inflation_Adjusted) AS Copper_Price_Inflation_Adjusted_variance, #Varaince = '7338403.0587851545'
VARIANCE(Iron_Price_Inflation_Adjusted) AS Iron_Price_Inflation_Adjusted_variance, #Varaince = '2081388.43490492'
VARIANCE(Steel_Price_Inflation_Adjusted) AS Steel_Price_Inflation_Adjusted_variance, #Varaince = '2021387.7971597868'
VARIANCE(Price_Chromium_Adjusted) AS Price_Chromium_Adjusted_variance #Varaince = '2093088.81048036'
FROM metalminerals;

#Third Moment Business Decision / Skewness#
SELECT
(
SUM(POWER(Price_Aluminium_per_Ton - (SELECT AVG(Price_Aluminium_per_Ton) FROM metalminerals),3))/
(COUNT(*) * POWER((SELECT STDDEV(Price_Aluminium_per_Ton) FROM metalminerals),3))
) AS skewness_Price_Aluminium_per_Ton,  # Skewness = '-0.03592017375834465'

(
SUM(POWER(Price_Tin_per_Ounce - (SELECT AVG(Price_Tin_per_Ounce) FROM metalminerals),3))/
(COUNT(*) * POWER((SELECT STDDEV(Price_Tin_per_Ounce) FROM metalminerals),3)))
 AS skewness_Price_Tin_per_Ounce, # Skewness = '0.01632801828486129'

(
SUM(POWER(Price_Copper_per_Ton - (SELECT AVG(Price_Copper_per_Ton) FROM metalminerals),3))/
(COUNT(*) * (POWER((SELECT STDDEV(Price_Copper_per_Ton) FROM metalminerals),3)))
)AS skewness_Price_Copper_per_Ton, # Skewness = '0.001183266878513344'

(
SUM(POWER(Price_Iron_per_Ounce - (SELECT AVG(Price_Iron_per_Ounce) FROM metalminerals),3))/
(COUNT(*) * POWER((SELECT STDDEV(Price_Iron_per_Ounce) FROM metalminerals),3))
) AS Skewness_Price_Iron_per_Ounce, # Skewness = '-0.04273984958322576'

(
SUM(POWER(Price_Steel_per_Ton - (SELECT AVG(Price_Steel_per_Ton) FROM metalminerals),3))/
(COUNT(*) * POWER((SELECT STDDEV(Price_Steel_per_Ton) FROM metalminerals),3))
) AS Skewnewss_Price_Steel_per_Ton, # Skewness = '0.0036776759731405534'

(
SUM(POWER(Inflation_Rate_Percentage - (SELECT AVG(Inflation_Rate_Percentage) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Inflation_Rate_Percentage) FROM metalminerals), 3))
) AS skewness_inflation_rate_percentage, # Skewness = '0.017069327261195377'

(
SUM(POWER(Aluminium_Price_Inflation_Adjusted - (SELECT AVG(Aluminium_Price_Inflation_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Aluminium_Price_Inflation_Adjusted) FROM metalminerals), 3))
) AS skewness_aluminium_price, # Skewness = '0.06705703682439564'

(
SUM(POWER(Tin_Price_Inflation_Adjusted - (SELECT AVG(Tin_Price_Inflation_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Tin_Price_Inflation_Adjusted) FROM metalminerals), 3))
) AS skewness_tin_price, # Skewness = '0.039223631800085416'

(
SUM(POWER(Copper_Price_Inflation_Adjusted - (SELECT AVG(Copper_Price_Inflation_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Copper_Price_Inflation_Adjusted) FROM metalminerals), 3))
) AS skewness_copper_price, # Skewness = '8.598237366271075'

(
SUM(POWER(Iron_Price_Inflation_Adjusted - (SELECT AVG(Iron_Price_Inflation_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Iron_Price_Inflation_Adjusted) FROM metalminerals), 3))
) AS skewness_iron_price, # Skewness = '-0.09378807242676285'

(
SUM(POWER(Steel_Price_Inflation_Adjusted - (SELECT AVG(Steel_Price_Inflation_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Steel_Price_Inflation_Adjusted) FROM metalminerals), 3))
) AS skewness_steel_price, # Skewness = '0.033527133122720244'

(
SUM(POWER(Price_Chromium_Adjusted - (SELECT AVG(Price_Chromium_Adjusted) FROM metalminerals), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Chromium_Adjusted) FROM metalminerals), 3))
) AS skewness_price_chromium # Skewness = '0.0346821791177706'
FROM metalminerals;


#Fourth Moment Business Decision / Kurtosis#
SELECT
(
(SUM(POWER(Price_Aluminium_per_Ton - (SELECT AVG(Price_Aluminium_per_Ton) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Aluminium_per_Ton) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Aluminium_per_Ton, #Kurtosis = '-1.3096003397401503'

(
(SUM(POWER(Price_Tin_per_Ounce - (SELECT AVG(Price_Tin_per_Ounce) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Tin_per_Ounce) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Tin_per_Ounce, #Kurtosis = '-1.2884940704458716'

(
(SUM(POWER(Price_Copper_per_Ton - (SELECT AVG(Price_Copper_per_Ton) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Copper_per_Ton) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Copper_per_Ton, #Kurtosis = '-1.2673663003020839'

(
(SUM(POWER(Price_Iron_per_Ounce - (SELECT AVG(Price_Iron_per_Ounce) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Iron_per_Ounce) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Iron_per_Ounce, #Kurtosis = '-1.33122361692201'

(
(SUM(POWER(Price_Steel_per_Ton - (SELECT AVG(Price_Steel_per_Ton) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Steel_per_Ton) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Steel_per_Ton, #Kurtosis = '-1.3043933449305642'

(
(SUM(POWER(Inflation_Rate_Percentage - (SELECT AVG(Inflation_Rate_Percentage) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Inflation_Rate_Percentage) FROM metalminerals), 4))) - 3
) AS kurtosis_Inflation_Rate_Percentage, #Kurtosis =  '-1.2372478469458805'

(
(SUM(POWER(Aluminium_Price_Inflation_Adjusted - (SELECT AVG(Aluminium_Price_Inflation_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Aluminium_Price_Inflation_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Aluminium_Price_Inflation_Adjusted, #Kurtosis = '-1.2968893417025367'

(
(SUM(POWER(Tin_Price_Inflation_Adjusted - (SELECT AVG(Tin_Price_Inflation_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Tin_Price_Inflation_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Tin_Price_Inflation_Adjusted, #Kurtosis = '-1.2102394557528873'
(
(SUM(POWER(Copper_Price_Inflation_Adjusted - (SELECT AVG(Copper_Price_Inflation_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Copper_Price_Inflation_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Copper_Price_Inflation_Adjusted, #Kurtosis = '111.98940940399162'

(
(SUM(POWER(Iron_Price_Inflation_Adjusted - (SELECT AVG(Iron_Price_Inflation_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Iron_Price_Inflation_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Iron_Price_Inflation_Adjusted, #Kurtosis =  '-1.3322062981391836'

(
(SUM(POWER(Steel_Price_Inflation_Adjusted - (SELECT AVG(Steel_Price_Inflation_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Steel_Price_Inflation_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Steel_Price_Inflation_Adjusted, #Kurtosis = '-1.208979595674701'
 
(
(SUM(POWER(Price_Chromium_Adjusted - (SELECT AVG(Price_Chromium_Adjusted) FROM metalminerals), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Price_Chromium_Adjusted) FROM metalminerals), 4))) - 3
) AS kurtosis_Price_Chromium_Adjusted #Kurtosis = '-1.2973577176703752'
FROM metalminerals;


# Preprocessing #
#Zero & near Zero Variance#

SELECT
VARIANCE(Price_Aluminium_per_Ton) AS Price_Iron_per_Ounce_variance
FROM metalminerals;

#Missing Values#
SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Aluminium_per_Ton IS NULL THEN 1 ELSE 0 END) AS Price_Aluminium_per_Ton_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Tin_per_Ounce IS NULL THEN 1 ELSE 0 END) AS Price_Tin_per_Ounce_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Copper_per_Ton IS NULL THEN 1 ELSE 0 END) AS Price_Copper_per_Ton_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Iron_per_Ounce IS NULL THEN 1 ELSE 0 END) AS Price_Iron_per_Ounce_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Steel_per_Ton IS NULL THEN 1 ELSE 0 END) AS Price_Steel_per_Ton_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Inflation_Rate_Percentage IS NULL THEN 1 ELSE 0 END) AS Inflation_Rate_Percentage_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Aluminium_Price_Inflation_Adjusted IS NULL THEN 1 ELSE 0 END) AS Aluminium_Price_Inflation_Adjusted_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Tin_Price_Inflation_Adjusted IS NULL THEN 1 ELSE 0 END) AS Tin_Price_Inflation_Adjusted_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Copper_Price_Inflation_Adjusted IS NULL THEN 1 ELSE 0 END) AS Copper_Price_Inflation_Adjusted_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Iron_Price_Inflation_Adjusted IS NULL THEN 1 ELSE 0 END) ASIron_Price_Inflation_Adjusted_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Steel_Price_Inflation_Adjusted IS NULL THEN 1 ELSE 0 END) AS Steel_Price_Inflation_Adjusted_missing
FROM metalminerals;

SELECT
COUNT(*) AS total_rows,
SUM(CASE WHEN Price_Chromium_Adjusted IS NULL THEN 1 ELSE 0 END) ASPrice_Chromium_Adjusted_missing
FROM metalminerals;

# Transformation
SELECT
Price_Aluminium_per_Ton, 
LOG(Price_Aluminium_per_Ton 
) AS Price_Aluminium_per_Ton_log,
SQRT(Price_Aluminium_per_Ton
) AS Price_Aluminium_per_Ton_sqrt
FROM metalminerals;

SELECT
Price_Aluminium_per_Ton, 
LOG(Price_Aluminium_per_Ton 
) AS Price_Aluminium_per_Ton_log,
SQRT(Price_Aluminium_per_Ton
) AS Price_Aluminium_per_Ton_sqrt
FROM metalminerals;


SELECT
Price_Tin_per_Ounce, 
LOG(Price_Tin_per_Ounce 
) AS Price_Tin_per_Ounce_log,
SQRT(Price_Tin_per_Ounce
) AS Price_Tin_per_Ounce_sqrt
FROM metalminerals;


SELECT
Price_Copper_per_Ton, 
LOG(Price_Copper_per_Ton 
) AS Price_Copper_per_Ton_log,
SQRT(Price_Copper_per_Ton
) AS Price_Copper_per_Ton_sqrt
FROM metalminerals;


SELECT
Price_Iron_per_Ounce, 
LOG(Price_Iron_per_Ounce 
) AS Price_Iron_per_Ounce_log,
SQRT(Price_Iron_per_Ounce
) AS Price_Iron_per_Ounce_sqrt
FROM metalminerals;


SELECT
Price_Steel_per_Ton, 
LOG(Price_Steel_per_Ton 
) AS Price_Steel_per_Ton_log,
SQRT(Price_Steel_per_Ton
) AS Price_Steel_per_Ton_sqrt
FROM metalminerals;


SELECT
Inflation_Rate_Percentage, 
LOG(Inflation_Rate_Percentage 
) AS Inflation_Rate_Percentage_log,
SQRT(Inflation_Rate_Percentage
) AS Inflation_Rate_Percentage_sqrt
FROM metalminerals;


SELECT
Aluminium_Price_Inflation_Adjusted, 
LOG(Aluminium_Price_Inflation_Adjusted 
) AS Aluminium_Price_Inflation_Adjusted_log,
SQRT(Aluminium_Price_Inflation_Adjusted
) AS Aluminium_Price_Inflation_Adjusted_sqrt
FROM metalminerals;


SELECT
Tin_Price_Inflation_Adjusted, 
LOG(Tin_Price_Inflation_Adjusted 
) AS Tin_Price_Inflation_Adjusted_log,
SQRT(Tin_Price_Inflation_Adjusted
) AS Tin_Price_Inflation_Adjusted_sqrt
FROM metalminerals;


SELECT
Copper_Price_Inflation_Adjusted, 
LOG(Copper_Price_Inflation_Adjusted 
) AS Copper_Price_Inflation_Adjusted_log,
SQRT(Copper_Price_Inflation_Adjusted
) AS Copper_Price_Inflation_Adjusted_sqrt
FROM metalminerals;


SELECT
Iron_Price_Inflation_Adjusted, 
LOG(Iron_Price_Inflation_Adjusted 
) AS Iron_Price_Inflation_Adjusted_log,
SQRT(Iron_Price_Inflation_Adjusted
) ASIron_Price_Inflation_Adjusted_sqrt
FROM metalminerals;


SELECT
Steel_Price_Inflation_Adjusted, 
LOG(Steel_Price_Inflation_Adjusted 
) AS Steel_Price_Inflation_Adjusted_log,
SQRT(Steel_Price_Inflation_Adjusted
) AS Steel_Price_Inflation_Adjusted_sqrt
FROM metalminerals;


SELECT
Price_Chromium_Adjusted, 
LOG(Price_Chromium_Adjusted 
) AS Price_Chromium_Adjusted_log,
SQRT(Price_Chromium_Adjusted
) AS Price_Chromium_Adjusted_sqrt
FROM metalminerals;








