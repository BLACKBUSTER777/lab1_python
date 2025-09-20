import importlib


def test_task00_distance():
    module = importlib.import_module("task01")
    result = module.solve()
    assert "Moscow" in result
    assert "London" in result
    assert "Paris" in result
    assert result["Moscow"]["Moscow"] == 0


def test_task01_circle():
    module = importlib.import_module("task02")
    result = module.solve()
    assert round(result["area"], 4) == 5541.7694
    assert result["point1_inside"] is True
    assert result["point2_inside"] is False


def test_task02_expression():
    module = importlib.import_module("task03")
    result = module.solve()
    assert result == 25


def test_task04_movies():
    module = importlib.import_module("task04")
    result = module.solve()
    assert isinstance(result, list)
    assert result[0].startswith("Терминатор")
    assert "Назад" in result[1]


def test_task04_family():
    module = importlib.import_module("task05")
    result = module.solve()
    assert result["father_height"] > 0
    assert result["total_height"] >= result["father_height"]


def test_task05_zoo():
    module = importlib.import_module("task06")
    result = module.solve()
    assert "bear" in result["zoo"]
    assert result["lion_cell"] == result["zoo"].index("lion") + 1
    assert result["lark_cell"] == result["zoo"].index("lark") + 1


def test_task06_songs():
    module = importlib.import_module("task07")
    result = module.solve()
    assert round(result["list_time"], 2) == 14.93
    assert round(result["dict_time"], 2) == 13.49


def test_task07_secret():
    module = importlib.import_module("task08")
    result = module.solve()
    assert isinstance(result, str)
    assert len(result.split()) == 5  # должно быть 5 слов


def test_task08_flowers():
    module = importlib.import_module("task09")
    result = module.solve()
    assert "ромашка" in result["all"]
    assert result["both"] == {"одуванчик", "ромашка"}
    assert isinstance(result["garden_only"], set)
    assert isinstance(result["meadow_only"], set)


def test_task09_sweets():
    module = importlib.import_module("task10")
    result = module.solve()
    assert "печенье" in result
    assert any(shop["shop"] == "пятерочка" for shop in result["печенье"])
    assert isinstance(result["конфеты"], list)


def test_task10_store():
    module = importlib.import_module("task11")
    result = module.solve()
    assert "Лампа" in result
    assert result["Лампа"]["quantity"] == 27
    assert result["Стол"]["quantity"] == 54
    assert result["Диван"]["quantity"] == 3
    assert result["Стул"]["quantity"] == 105
    assert result["Стул"]["cost"] > 0
