# Contracts
PROTO_DIR=./protos

# APIService
API_PROTO=$(PROTO_DIR)/apiservice.proto
API_OUT=./services/ApiService/api
API_AUTH_OUT=./services/ApiService/auth

# AuthService
AUTH_PROTO=$(PROTO_DIR)/authservice.proto
AUTH_OUT=./services/AuthService/server

# UserService
USER_PROTO=$(PROTO_DIR)/userservice.proto
USER_OUT=./services/UserService/Services/generated

# Go protoc options
GO_OPT=import
GRPC_OPT=source_relative


# testing
TEST_DIR=./test
API_TEST_OUT=./test/test_ApiService
AUTH_TEST_OUT=./test/test_AuthService

up: codegen
	docker-compose up -d --build

down:
	docker-compose down

codegen: codegen_api codegen_auth
	echo "Generating all"

# Generate Code for APIService
codegen_api:
	# APIService 
	protoc -I=$(PROTO_DIR) --go_out=$(API_OUT) --go_opt=paths=source_relative \
    --go-grpc_out=$(API_OUT) --go-grpc_opt=paths=source_relative \
    $(API_PROTO)

	# AuthService (Client)  --go_opt=paths=source_relative
	protoc -I=$(PROTO_DIR) --go_out=$(API_AUTH_OUT) --go_opt=paths=source_relative \
    --go-grpc_out=$(API_AUTH_OUT) --go-grpc_opt=paths=source_relative \
    $(AUTH_PROTO)
	

codegen_auth:
	# AuthService
	python -m grpc_tools.protoc -I=$(PROTO_DIR) \
	--python_out=$(AUTH_OUT) \
	--grpc_python_out=$(AUTH_OUT) \
	$(AUTH_PROTO)

	# APIService (.proto import dependency)
	python -m grpc_tools.protoc -I=$(PROTO_DIR) \
	--python_out=$(AUTH_OUT) \
	--grpc_python_out=$(AUTH_OUT) \
	$(API_PROTO)


# Run all unittests (currently broken until someone answers my stackoverflow)
# in the meantime, test files can be run manually
test: build_test
	python -m unittest discover $(TEST_DIR)

# Generate all code needed for test clients
build_test:
	# APIService
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(API_TEST_OUT) --grpc_python_out=$(API_TEST_OUT) $(API_PROTO)

	# AuthService
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(AUTH_TEST_OUT) --grpc_python_out=$(AUTH_TEST_OUT) $(AUTH_PROTO)
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(AUTH_TEST_OUT) --grpc_python_out=$(AUTH_TEST_OUT) $(API_PROTO)

# Use me for suggestions when things aren't working
dammit: damn_go damn_cs damn_py
	@echo "====== All ======"
	@echo "Are you using the right shell?"
	@echo "Have you restarted vscode?"
	@echo "Have you regenerated code?"

damn_go:
	@echo "====== Go ======"
	@echo "check GO111MODULE"
	@echo "check go.mod module name, and import <modulename>/package"
	@echo "restart and update go tools... gopls"

damn_cs:
	@echo "====== C# ======"
	@echo "restart Omnisharp (ctrl + shift + p > restart omni...)"
	@echo "dotnet restore"
	@echo "dotnet build"

damn_py:
	@echo "====== Python ======"
	@echo "relative imports?"
	@echo "__init__.py?"