import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)
        water = [[float('inf') for _ in range(N)] for _ in range(N)]
        water[0][0] = grid[0][0]

        q = [(water[0][0], 0, 0)]
        heapq.heapify(q)
        while q:
            w, row, col = heapq.heappop(q)
            if w > water[row][col]:
                continue
            if row == N-1 and col == N-1:
                break
            for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= r < N and 0 <= c < N:
                    nw = max(grid[r][c], water[row][col])
                    if nw < water[r][c]:
                        water[r][c] = nw
                        heapq.heappush(q, (nw, r, c))

        # for row in water:
        #     print(row)
        return water[N-1][N-1]


s = Solution()
print(s.swimInWater([[0,2],[1,3]]))
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
print(s.swimInWater([[3,2],[0,1]]))
print(s.swimInWater([[575,2059,1205,840,349,2190,1833,1387,1974,1251,504,413,1746,1555,1207,1334,1143,863,67,2053,1758,251,299,1088,350,506,2060,1137,1054,993,1919,2252,1930,592,1854,142,343,677,778,1633,850,2367,1239,407,134,267,1328,1086,2297],[812,624,1541,1566,244,1955,1733,399,1999,1506,507,53,1792,1762,998,1868,782,367,861,2282,1452,568,2233,1739,495,1508,1680,54,2162,2097,763,2015,2047,683,1960,1823,1662,2289,1491,131,2321,941,1810,1724,2120,1503,1875,2128,2057],[207,1811,1227,1603,1959,219,536,1192,332,1718,985,698,1817,960,432,1145,1028,1688,711,29,1826,494,1150,762,737,2086,232,220,2041,1169,1874,919,708,35,447,2074,1018,1316,1809,1107,758,945,1072,1993,328,1488,1497,1863,2275],[1672,791,68,324,591,224,2177,395,412,2061,1133,170,1029,71,1685,1929,1156,2327,1708,387,284,1267,777,1592,1411,1915,1968,1880,1471,2065,748,405,195,318,1112,766,1258,362,564,621,1175,2302,1098,2188,381,742,600,1845,1438],[283,842,33,1813,1025,1902,355,46,881,171,2026,228,1650,961,1644,1433,656,2000,717,1060,1849,241,2317,989,687,2211,1927,1197,2052,496,925,1042,2345,968,264,933,1331,571,844,1819,2195,1273,211,1103,2329,4,1928,906,1614],[1673,1296,819,1149,1421,1246,2342,307,951,1212,1624,2105,323,901,1195,2024,1597,1877,1122,2392,1824,1903,1007,2214,433,185,85,1404,1789,887,1295,646,1147,1434,1980,428,1181,2010,1357,1215,276,1342,936,1330,792,897,1712,193,2323],[1093,1512,1259,625,1275,1552,1354,1234,1781,441,145,1282,783,1131,1748,374,1697,807,1405,1500,1623,959,1067,2219,1091,88,1565,161,1737,833,944,562,1933,1534,898,1496,186,2142,781,347,2319,558,1109,702,147,82,1182,398,1695],[602,282,2088,429,1601,843,1040,102,2048,6,1881,870,2279,487,2381,583,1090,2229,1366,1199,105,866,290,811,1114,1444,1177,2038,1779,1607,1871,30,2331,1080,1517,111,492,1284,1289,148,2034,657,1372,255,2004,331,1168,1546,904],[1271,2066,461,217,1755,581,340,1221,1100,1610,1690,549,1051,1563,598,2239,2027,1110,2322,1952,34,767,516,92,1992,410,966,1129,1655,197,1279,1165,1397,2113,1914,155,980,513,688,1076,301,1026,2369,11,2176,291,1470,223,2157],[1113,2398,1668,1075,1857,1202,1003,424,55,2019,2133,1766,550,249,609,969,235,1286,175,121,1185,1851,2218,2165,2363,2196,2106,327,2238,802,1002,909,774,1399,1821,772,2095,663,586,2077,1645,2240,2191,2359,2082,368,627,138,2268],[278,2212,728,1608,2260,1593,451,152,1196,594,320,2121,2231,25,2108,2338,159,57,511,1260,529,2002,490,1925,912,618,2028,252,430,654,605,1161,1694,649,1722,309,482,1938,2102,2160,1440,1483,1363,578,218,1752,1537,1801,1838],[1415,1971,1686,302,1747,1340,2107,1280,2370,1249,883,2269,209,1368,1401,1550,1973,377,1322,2259,1861,2243,357,1618,1560,1865,1376,2248,1244,2067,1347,615,1916,2115,2333,1549,1117,1627,2130,1184,1521,1571,1542,1872,1532,1706,1783,1081,1850],[846,215,90,1303,786,554,814,365,358,1536,2305,7,2167,59,1270,1213,1448,2385,2039,1493,1803,557,74,939,2008,1511,1580,2154,1180,1469,2151,994,2382,1423,1554,603,440,2153,78,914,1276,604,1058,923,76,394,1302,1774,1575],[1776,49,5,20,1687,1264,1379,43,1362,638,2119,1642,402,2226,790,946,667,457,1474,1023,1679,103,1190,756,2200,1522,1820,359,1735,12,2179,372,200,2225,1740,94,240,1793,79,982,2062,287,1019,865,799,2145,325,1274,1307],[1513,1770,189,648,794,2011,2109,1065,880,572,523,1127,996,1068,764,619,1778,634,617,1667,1582,2390,486,164,1396,1436,47,1043,1876,1908,722,336,595,921,403,2266,2230,1756,2210,2341,1079,1457,899,16,679,313,1804,1371,1705],[611,1707,1786,1831,1860,369,845,2283,1569,1683,1030,873,2318,824,1666,1056,173,1346,1606,1896,673,576,1765,2030,1348,40,1367,1299,2199,2094,2299,125,1432,2328,1359,1725,1617,1375,160,1095,2058,311,2156,2346,601,1594,2355,48,1917],[1795,269,1317,1553,206,1413,1097,1738,1157,352,1905,1717,1105,548,1078,710,2186,1559,2303,75,681,32,129,1211,1124,1635,454,891,1321,633,694,1975,888,869,1253,1577,41,829,816,1102,1389,66,522,1345,875,258,1223,118,1238],[163,1458,1383,1799,1638,797,2175,475,585,2356,1041,1219,1420,894,1406,2138,1230,108,1300,130,2253,480,967,1479,1664,204,1094,2181,1634,178,561,122,2150,418,1625,1944,2127,1498,1266,338,1082,632,1369,106,1557,100,1807,1248,587],[1412,540,1008,1337,801,242,1407,1651,225,709,2139,1178,712,158,2193,975,981,2204,2206,2324,1250,439,546,1013,1116,2313,1048,479,862,1268,1885,1796,2070,1862,101,1675,813,1888,356,1431,1074,2183,361,26,596,427,60,315,810],[1616,525,804,419,1329,1948,1768,1967,1590,669,1263,177,2308,2320,1620,1744,1657,2349,1583,1063,273,213,2185,2194,685,785,1108,729,827,1870,404,2396,650,277,2310,1684,1385,2081,2140,1480,2335,1449,1333,1591,417,1179,510,444,2245],[2291,805,2064,2187,260,2035,379,1564,1245,484,436,329,1567,1547,1297,854,979,1468,502,990,1736,1965,896,719,1715,2110,1729,671,2375,2072,2267,1222,696,1578,360,1757,1455,294,1430,151,168,401,1505,950,1989,1507,443,1538,354],[380,2045,920,246,1539,1911,1410,1890,623,1879,2180,1339,72,1208,231,1525,1101,187,1036,780,1400,1482,1226,2235,2372,2278,1805,1528,1516,1797,13,1669,363,415,208,1142,2043,234,458,58,1646,1585,1576,1719,2202,2222,1544,1188,254],[1024,986,713,1005,753,1523,2387,1319,1417,2161,44,597,2374,2078,1398,1894,2242,1487,384,1446,678,8,999,2232,1162,1636,2276,1787,1408,620,133,907,1384,446,555,99,543,1336,141,746,1961,317,858,995,1022,179,2340,724,2208],[1540,1361,1320,18,1841,1193,519,1038,389,743,1710,1602,947,1572,1661,1753,38,937,2168,2126,903,517,0,1391,2224,1031,956,902,279,233,1119,1478,675,1761,735,2031,184,2393,1855,1941,849,900,680,1418,2261,1834,692,3,2298],[1573,2020,1946,2152,2205,563,406,2021,760,1982,114,1166,2136,518,201,2312,238,272,527,423,1111,344,1066,1099,674,1462,697,1247,156,1349,838,1997,776,641,538,1700,1682,167,2220,1530,334,693,2117,761,1085,1364,530,1551,150],[1742,296,1306,1255,1772,1017,1561,512,1949,1035,2075,2164,2255,1545,2280,112,1164,1913,2159,348,1464,2311,1963,705,1984,1734,1629,958,608,2271,686,1032,1335,1622,239,1272,243,851,1435,136,2148,1314,1816,545,552,1285,212,1777,1909],[779,285,265,1956,2029,1504,182,651,335,2395,997,1784,973,834,1605,1386,1290,1370,227,754,676,1935,964,468,469,884,1723,612,1898,970,386,1429,1510,1016,1969,127,2343,1957,1445,2042,50,1790,689,2221,376,1985,86,2198,1261],[2353,1125,303,1134,2135,1858,1676,948,695,2307,1055,622,871,2116,1754,1788,1846,943,1210,146,2326,1654,660,1775,2084,877,2071,1767,885,580,19,83,2234,396,640,1298,330,828,1626,245,2055,1599,929,949,2085,210,1745,292,1931],[388,2357,174,661,1187,2001,1951,1136,157,798,113,730,1800,720,337,2147,408,1442,1027,1224,2376,89,1609,1126,521,639,1083,393,541,1373,1798,1693,425,1702,1791,1964,931,831,716,2378,599,2228,149,1476,1071,411,1895,2005,1332],[248,1981,823,1818,2389,1344,298,2184,1204,497,1836,1257,2192,1782,1802,800,1460,1889,1174,551,1194,1461,470,1292,868,952,749,848,445,237,913,535,1262,1901,1696,1360,1242,574,974,765,483,1936,1118,2314,1304,2096,1918,1628,1064],[1096,351,1883,2100,498,847,1780,2122,42,1228,353,2131,954,2309,1200,2304,1598,556,93,1543,1611,15,537,1531,453,1053,2158,1010,1481,1600,1711,431,1443,91,1146,293,2265,1613,524,1456,449,478,2049,383,859,2351,80,253,21],[481,2377,1352,1581,567,647,1639,1380,2296,1419,2332,1154,270,1356,2264,553,855,1287,1847,1225,889,1988,10,2044,1962,1191,940,2301,741,915,2262,577,1277,1353,420,1501,2286,2091,2347,1104,1151,2197,531,1318,560,230,1231,1524,938],[1692,1986,2112,256,288,1160,1822,659,1637,1465,205,180,935,259,45,658,2300,1947,310,1556,268,1891,700,977,1529,1773,1393,1000,1009,135,198,1937,589,1014,820,2169,176,1852,140,2068,95,485,2013,1900,2171,2285,2394,2093,1691],[1751,1867,1312,1750,1198,916,1141,1924,1402,2388,2006,2368,922,1106,1232,153,788,2330,704,1,110,2189,261,77,1764,52,2272,1689,1283,1678,1214,526,2362,1020,1382,1236,17,1309,796,1825,2007,1514,882,236,1148,467,455,751,721],[1326,1489,2012,104,1171,1621,2383,1153,727,1403,62,1996,1562,682,2104,1135,2223,9,942,886,1381,400,2174,718,385,1358,493,2149,1243,1288,1308,312,588,643,971,707,1643,1427,1596,473,1394,2009,628,652,1943,1923,1589,2373,65],[1502,1595,2172,2236,613,2069,203,988,459,1233,818,715,84,2274,822,1832,191,2037,154,1206,2017,1972,1878,1189,1414,2352,370,515,662,1665,2080,1473,321,2144,1325,2315,978,1907,2056,397,636,1677,464,934,139,1395,2361,2379,808],[2360,1486,2209,542,2237,665,1158,488,670,63,514,1604,144,532,183,1034,965,635,196,1033,872,169,1170,280,664,1726,547,1494,96,1341,2281,314,1388,1428,1293,1365,860,1808,1201,1884,1424,637,1172,81,51,2277,1887,1837,1001],[308,1240,1827,37,2215,2032,2203,2290,867,963,2207,1351,2051,466,503,2054,221,1730,1392,784,2217,1278,14,286,1409,699,2371,1061,1121,115,1451,316,1011,460,806,976,1648,1998,2114,1713,375,1173,247,2003,1921,1670,1466,505,416],[566,1087,1920,1254,1050,1843,1584,1475,1720,1447,825,2257,768,1741,2016,1004,745,1039,1128,773,1437,1144,1070,190,2201,1721,1374,606,731,1812,1495,1378,732,489,1477,1343,1218,70,1904,2073,263,499,1977,306,1991,2087,629,607,1183],[1892,1979,1897,879,1844,275,1518,1859,2132,1130,1806,2134,1217,1839,1425,1527,691,1574,1138,757,1241,2251,905,528,755,835,448,2014,300,770,2365,1586,442,793,1864,1044,1163,342,703,1656,162,1338,73,1453,1899,874,1291,2358,1073],[1970,2270,222,736,1632,645,653,2076,119,1659,911,2025,435,1587,1848,738,1046,2246,2364,1815,1966,1709,610,1235,378,456,972,1698,957,684,2166,1731,690,1526,582,1115,500,2397,826,2293,2386,2325,1313,2,1932,789,932,2033,955],[188,1485,1699,2287,1047,2344,1062,132,631,2241,1630,1281,137,1701,1139,64,655,1568,2384,642,787,559,2123,1159,2336,701,1704,271,1167,437,1716,1978,1660,391,1515,533,876,1120,117,471,192,992,501,725,841,1509,366,1084,1749],[832,421,2101,1140,305,1759,1426,821,1990,1057,345,109,341,339,2124,852,1077,1995,1037,1069,165,1484,1910,584,1355,1856,382,910,739,1743,508,462,2018,856,924,2295,1647,1588,626,266,817,373,491,1216,2129,1052,590,759,1814],[837,962,2163,1829,2155,544,1132,1558,2247,274,463,2213,853,1324,1390,1703,1459,2254,983,2250,87,1942,918,1886,2023,1641,1089,1652,1728,36,1771,987,326,1674,726,2273,509,23,262,1785,714,1853,928,371,1830,752,2040,2216,107],[2348,229,24,1732,1472,1015,1840,1842,414,953,202,333,750,124,199,2036,1866,815,2103,2182,2244,289,1265,452,1176,2089,917,257,2083,422,569,630,539,723,2256,2284,409,1570,1059,908,56,1490,434,1763,322,2258,893,319,166],[2098,836,1499,1045,706,1906,1021,116,1520,2288,2090,1939,890,1454,1976,1294,672,1548,593,1006,2380,2249,2178,809,476,1926,1305,1535,27,346,1987,1220,666,123,864,120,1649,1653,1315,616,2063,1912,769,1463,450,216,2125,392,426],[214,1203,1828,2292,2391,1794,2111,1301,2294,1229,1092,2079,2316,2143,1953,803,2350,1237,775,2263,927,172,1631,181,1873,2337,984,744,304,1950,297,1714,61,2046,1533,534,1256,579,477,474,2050,740,2099,364,1152,1049,830,644,126],[1327,1934,1209,250,2141,1681,1123,194,2170,98,1252,1983,795,2022,878,1882,1658,1945,39,97,69,1269,390,1416,2400,1663,857,565,1422,1727,1893,2118,747,892,668,226,438,1012,1492,1310,733,1922,2334,2366,1769,2173,1441,1377,930],[570,2227,1640,771,1450,1311,1954,1994,28,1467,295,1323,2092,573,1612,926,895,2339,1671,520,1835,1760,2137,281,472,2399,2306,128,1579,1940,2146,143,465,839,1186,1350,1869,31,1958,22,1615,991,1439,2354,1155,1619,1519,734,614]]))