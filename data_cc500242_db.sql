LOCK TABLES `viaje` WRITE;
/*!40000 ALTER TABLE `viaje` DISABLE KEYS */;
INSERT INTO `viaje` (`id`, `origen`, `destino`, `fecha_ida`, `fecha_regreso`, `kilos_disponible`, `espacio_disponible`, `email_viajero`, `celular_viajero`) VALUES
(1, 258, 252, '2021-06-19 04:00:00', '2022-09-30 03:00:00', 2, 2, 'elisapargam@gmail.com', 'hola'),
(2, 258, 252, '2021-06-19 04:00:00', '2022-09-30 03:00:00', 2, 2, 'elisapargam@gmail.com', 'hola'),
(3, 252, 252, '2021-06-19 04:00:00', '2022-09-30 03:00:00', 2, 2, 'elisapargam@gmail.com', 'hola'),
(4, 244, 245, '2021-09-18 03:00:00', '2022-09-18 03:00:00', 1, 2, 'elisa.parga@student-cs.fr', '+56912345678'),
(5, 242, 249, '2019-07-19 04:00:00', '2019-10-09 03:00:00', 3, 1, 'silvia.leivamirande@gmail.com', ''),
(6, 253, 242, '2019-06-19 04:00:00', '2020-09-18 03:00:00', 2, 2, 'elisa.parga@ug.uchile.cl', '+56987654321'),
(7, 253, 242, '2019-06-19 04:00:00', '2020-09-18 03:00:00', 2, 2, 'elisa.parga@ug.uchile.cl', '+56987654321'),
(8, 252, 251, '2019-06-16 04:00:00', '2020-03-15 03:00:00', 2, 1, 'elisa.parga@ug.uchile.cl', ''),
(9, 250, 255, '2020-05-15 04:00:00', '2021-03-12 03:00:00', 3, 1, 'silvia.leivamirande@gmail.com', ''),
(10, 249, 252, '2020-06-19 04:00:00', '2020-10-10 03:00:00', 2, 3, 'elisa_parga29@hotmail.com', '+56912345678'),
(11, 251, 252, '2019-06-07 04:00:00', '2020-10-10 03:00:00', 3, 3, 'elisapargam@gmail.com', '+56912345678'),
(12, 258, 260, '2022-09-18 03:00:00', '2022-11-04 03:00:00', 2, 2, 'silvia.leivamirande@gmail.com', '+56987654321'),
(13, 435, 259, '2014-06-19 04:00:00', '2014-07-19 04:00:00', 1, 1, 'silvia.leivamirande@gmail.com', '+56996743585'),
(14, 312, 313, '2019-09-16 03:00:00', '2020-01-02 03:00:00', 5, 3, 'elisa.parga@student-cs.fr', '+56996547352'),
(15, 318, 258, '2021-03-15 03:00:00', '2021-04-19 04:00:00', 2, 1, 'elisa.parga@ug.uchile.cl', '+56965387654'),
(16, 317, 453, '2021-10-17 03:00:00', '2021-12-12 03:00:00', 3, 1, 'elisa_parga29@hotmail.com', '+56956378923');
/*!40000 ALTER TABLE `viaje` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `encargo` WRITE;
/*!40000 ALTER TABLE `encargo` DISABLE KEYS */;
INSERT INTO `encargo` (`id`, `descripcion`, `espacio`, `kilos`, `origen`, `destino`, `email_encargador`, `celular_encargador`) VALUES
(37, 'gato 1', 2, 1, 253, 252, 'elisa.parga@student-cs.fr', '+56987654321'),
(39, 'gato 3', 2, 1, 314, 323, 'elisa.parga@student-cs.fr', ''),
(40, 'gato 4', 1, 4, 308, 334, 'elisa_parga29@hotmail.com', ''),
(41, 'gato 5', 1, 2, 344, 343, 'elisapargam@gmail.com', ''),
(42, 'test', 3, 6, 385, 283, 'elisa@elisa.cl', ''),
(43, 'test', 3, 6, 459, 334, 'elisa@elisa.cl', ''),
(44, 'test', 3, 6, 403, 280, 'elisa@elisa.cl', ''),
(45, 'Hola', 2, 2, 332, 333, 'elisa.parga@ug.uchile.cl', ''),
(46, 'Hola', 2, 2, 456, 338, 'elisa.parga@ug.uchile.cl', '');
/*!40000 ALTER TABLE `encargo` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `foto` WRITE;
/*!40000 ALTER TABLE `foto` DISABLE KEYS */;
INSERT INTO `foto` (`id`, `ruta_archivo`, `nombre_archivo`, `encargo_id`) VALUES
(28, '/media/', 'd2b4bf78b8b86cf7b1ab3184e77480d538d9e6af1d6e8e6b91162b4e4879c7b8b4ba61363ab9a332606e7b16670b76a4e1f97b05f4ec217be7cf3cb6bc9f95f3.jpg', 37),
(30, '/media/', 'ba5767caabceca4a0a87ad4815bf7ee71cab00a93550e5d8488ea0fbe215aef2b9e1d6ec5f738d9fa43589c66876209eb9b729d65bbf68efc9ee005cce9239db.jpg', 39),
(31, '/media/', 'f8a17857af81ca30e2fa71f14dc45326550e83e40574af7d24370e3f2afdafff261c5ebe66ecda227a3c8338a628da6962b4cf93f0c6fab31d3c78c7a3fff99a.jpg', 40),
(32, '/media/', '7e77af6a4b5406bc57897d0f2718538d7c0b1b22d0d58641d0bc489fc3b97705e200e48345fb3c43d96b419547db4f3355a986e423c474baf640379d245f1f80.jpg', 41),
(33, '/media/', '3783aee377579cae86ffbb1093fb618a5971397aba5b11e4971b143246fca6a66902b0a3035b1733d862c38d7e614a120a8bedc4cff1e1435a61c71f147ab5d6.jpg', 42),
(34, '/media/', '73561717ae7f1c36b7ba3582c4a6ec60aff16c13327ef4a4cdb74821d765484487a783d7429915ea00957312c0f790a3313a767bc1d248dea8271b27ac4a1b2b.jpg', 42),
(35, '/media/', '3783aee377579cae86ffbb1093fb618a5971397aba5b11e4971b143246fca6a66902b0a3035b1733d862c38d7e614a120a8bedc4cff1e1435a61c71f147ab5d6.jpg', 43),
(36, '/media/', '73561717ae7f1c36b7ba3582c4a6ec60aff16c13327ef4a4cdb74821d765484487a783d7429915ea00957312c0f790a3313a767bc1d248dea8271b27ac4a1b2b.jpg', 43),
(37, '/media/', '3783aee377579cae86ffbb1093fb618a5971397aba5b11e4971b143246fca6a66902b0a3035b1733d862c38d7e614a120a8bedc4cff1e1435a61c71f147ab5d6.jpg', 44),
(39, '/media/', '3783aee377579cae86ffbb1093fb618a5971397aba5b11e4971b143246fca6a66902b0a3035b1733d862c38d7e614a120a8bedc4cff1e1435a61c71f147ab5d6.jpg', 45),
(40, '/media/', '3783aee377579cae86ffbb1093fb618a5971397aba5b11e4971b143246fca6a66902b0a3035b1733d862c38d7e614a120a8bedc4cff1e1435a61c71f147ab5d6.jpg', 46);
/*!40000 ALTER TABLE `foto` ENABLE KEYS */;
UNLOCK TABLES;