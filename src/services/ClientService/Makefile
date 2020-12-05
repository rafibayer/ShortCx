run: build
	-docker rm -f shortcxcli
	docker run -d -p 80:80 --name shortcxcli shortcxtest

build:
	npx webpack
	docker build -t shortcxtest .

log:
	docker logs shortcxcli