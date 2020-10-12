#!/bin/bash

git config core.autocrlf input # LF를 line ending으로 설정

git config commit.template docs/.gitmessage
