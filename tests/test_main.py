def test_main_output(capfd):
    from src import main

    main.main()
    captured = capfd.readouterr()
    assert "Hello from Jordanwright workspace" in captured.out
