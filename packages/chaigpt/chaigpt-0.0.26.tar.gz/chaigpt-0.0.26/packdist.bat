@REM @echo off
echo Are you sure you want to package and distribute the latest release of ChaiGPT?
pause

if exist %~dp0dist (
    rmdir /s /q %~dp0dist
)

if exist %~dp0requirements.txt (
    del %~dp0requirements.txt
)

pipreqs %~dp0src\chaigpt --savepath %~dp0requirements.txt
pipreqs %~dp0src\chaigpt --clean %~dp0requirements.txt

python %~dp0make_toml.py

pip install -U build
pushd %~dp0
python -m build
popd

pip install -U twine
twine check dist/*
@REM python -m twine upload dist/*

