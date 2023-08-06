@echo off

if exist %~dp0dist (
    rmdir /s /q %~dp0dist
)

if exist %~dp0requirements.txt (
    del %~dp0requirements.txt
)

pipreqs %~dp0src\chaigpt --savepath %~dp0requirements.txt
pipreqs %~dp0src\chaigpt --clean %~dp0requirements.txt

python %~dp0parse_dependencies.py
python %~dp0increment_version_number.py

pip install -U build
pushd %~dp0
python -m build
popd

pip install -U twine
twine check dist/*
python -m twine upload dist/*

