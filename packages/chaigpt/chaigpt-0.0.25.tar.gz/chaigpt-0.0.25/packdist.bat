echo Are you sure you want to package and distribute the latest release of ChaiGPT?
pause

if exist %~dp0dist (
    rmdir /s /q %~dp0dist
)

@REM if exist %~dp0requirements.txt (
@REM     del %~dp0requirements.txt
@REM )

@REM pipreqs %~dp0src\chaigpt --savepath %~dp0requirements.txt
@REM pipreqs %~dp0src\chaigpt --clean %~dp0requirements.txt

@REM python %~dp0make_toml.py

pip install -U build
pushd %~dp0
python -m build
popd

pip install -U twine
twine check dist/*
python -m twine upload dist/*

