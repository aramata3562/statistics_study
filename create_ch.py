import os
import json

def create_notebooks(directory, count):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, count + 1):
        filename = f'ch{i:02d}.ipynb'
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            content = {
                "cells": [],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 4
            }
            json.dump(content, f)

# 使用例

create_notebooks('/Users/taketoaramaki/study/statistics_study/統計学実践ワークブック', 32)

