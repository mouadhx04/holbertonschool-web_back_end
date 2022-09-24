-- All bands with Glam as their main style
-- ranked by their longevity
SELECT `band_name`, 
IFNULL(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands 
Where `style` Like '%Glam Rock%';