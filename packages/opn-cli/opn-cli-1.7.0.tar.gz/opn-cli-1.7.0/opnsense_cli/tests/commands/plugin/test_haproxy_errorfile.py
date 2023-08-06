from unittest.mock import patch, Mock
from opnsense_cli.commands.plugin.haproxy.errorfile import errorfile
from opnsense_cli.tests.commands.base import CommandTestCase


class TestHaproxyErrorfileCommands(CommandTestCase):
    def setUp(self):
        self._api_data_fixtures_reconfigure_OK = {
            "status": "ok"
        }
        self._api_data_fixtures_reconfigure_FAILED = {
            "status": "failed"
        }
        self._api_data_fixtures_configtest_OK = {
            "result": "Configuration file is valid\n\n\n"
        }
        self._api_data_fixtures_configtest_FAILED = {
            "result": "Configuration file is invalid\n\n\n"
        }
        self._api_data_fixtures_create_OK = {
            "result": "saved",
            "uuid": "85282721-934c-42be-ba4d-a93cbfda26af"
        }
        self._api_data_fixtures_create_ERROR = {
            "result": "failed",
            "validations": {'errorfile.description': 'Should be a string between 1 and 255 characters.'}
        }
        self._api_data_fixtures_update_OK = {
            "result": "saved"
        }
        self._api_data_fixtures_update_NOT_EXISTS = {
            "result": "failed"
        }
        self._api_data_fixtures_delete_NOT_FOUND = {
            "result": "not found"
        }
        self._api_data_fixtures_delete_OK = {
            "result": "deleted"
        }
        self._api_data_fixtures_list_EMPTY = {
            "haproxy": {
                "errorfiles": {
                    "errorfile": []
                }
            }
        }
        self._api_data_fixtures_list = self._read_json_fixture('plugin/haproxy/model_data.json')
        self._api_client_args_fixtures = [
            'api_key',
            'api_secret',
            'https://127.0.0.1/api',
            True,
            '~/.opn-cli/ca.pem',
            60
        ]

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_list(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            errorfile,
            [
                'list', '-o', 'plain', '-c',
                'uuid,name,description,code,content'
            ]
        )

        self.assertIn(
            (
                "a7dc8e54-c7c3-4aa4-a3de-b37d159a9c7a custom_error_500 My custom error messae x500 HTTP/1.0 503 "
                "Service Unavailable\n"
                "Cache-Control: no-cache\n"
                "Connection: close\n"
                "Content-Type: text/html\n\n"
                "<html> \n"
                "  <head>\n"
                "    <title>RARRR!!!!!</title>\n"
                "  </head> \n"
                "  <body style=\"font-family:Arial,Helvetica,sans-serif;\">\n"
                "    <div style=\"margin: 0 auto; width: 960px;\"> \n"
                "          <h2 >RAWR RAWR RAWR</h2>\n"
                "    </div>\n"
                "  </body> \n"
                "</html>\n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_list_EMPTY(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list_EMPTY,
            ],
            errorfile,
            ['list', '-o', 'plain']
        )

        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_show_NOT_FOUND(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            errorfile,
            ['show', 'b468c719-89db-45a8-bd02-b081246dc002']
        )
        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_show_EMPTY_STRING(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            errorfile,
            ['show', '']
        )
        self.assertIn("", result.output)

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_show(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_list,
            ],
            errorfile,
            [
                'show', 'a7dc8e54-c7c3-4aa4-a3de-b37d159a9c7a', '-o', 'plain', '-c',
                'name,description,code,content'
            ]
        )

        self.assertIn(
            (
                "custom_error_500 My custom error messae x500 HTTP/1.0 503 "
                "Service Unavailable\n"
                "Cache-Control: no-cache\n"
                "Connection: close\n"
                "Content-Type: text/html\n\n"
                "<html> \n"
                "  <head>\n"
                "    <title>RARRR!!!!!</title>\n"
                "  </head> \n"
                "  <body style=\"font-family:Arial,Helvetica,sans-serif;\">\n"
                "    <div style=\"margin: 0 auto; width: 960px;\"> \n"
                "          <h2 >RAWR RAWR RAWR</h2>\n"
                "    </div>\n"
                "  </body> \n"
                "</html>\n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_create_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_create_OK,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "create", "my_test_errorfile",
                "--code", "x400",
                "--description", "bad request",
                "--content",
                "Bad Request\n"
                "Cache-Control: no-cache\n"
                "Connection: close\n"
                "Content-Type: text/html\n\n"
                "<html> \n"
                "  <head>\n"
                "    <title>very bad request</title>\n"
                "  </head> \n"
                "  <body style=\"font-family:Arial,Helvetica,sans-serif;\">\n"
                "    <div style=\"margin: 0 auto; width: 960px;\"> \n"
                "          <h2>Bad Request</h2>\n"
                "    </div>\n"
                "  </body> \n"
                "</html>\n",
            ]
        )

        self.assertIn(
            (
                "saved \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_create_ERROR(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_create_ERROR,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "create", "my_test_errorfile",
                "--code", "x400",
                "--content", "400",
                "--description",
                "12001201200201200210202100210210201032183902140479314713905734095703457043570347503927504325702"
                "43957032457023475092357034257024357042375042382374t385784735238562586853498573957340957035734059"
                "7430573405943709750439754039754035974035743057403957403570439574390570435704397504375094375043975"

            ]
        )

        self.assertIn(
            (
                "Error: {'result': 'failed', 'validations': "
                "{'errorfile.description': 'Should be a string between 1 and 255 characters.'}}\n"
            ),
            result.output
        )
        self.assertEqual(1, result.exit_code)

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_update_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_update_OK,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "update", "a7dc8e54-c7c3-4aa4-a3de-b37d159a9c7a",
                "--description", "modified"
            ]
        )

        self.assertIn(
            (
                "saved \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_update_NOT_EXISTS(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_update_NOT_EXISTS,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "update", "99282721-934c-42be-ba4d-a93cbfda2644",
                "--description", "modified"
            ]
        )

        self.assertIn(
            (
                "Error: {'result': 'failed'}\n"
            ),
            result.output
        )
        self.assertEqual(1, result.exit_code)

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_delete_OK(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_delete_OK,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "delete", "a7dc8e54-c7c3-4aa4-a3de-b37d159a9c7a",
            ]
        )

        self.assertIn(
            (
                "deleted \n"
            ),
            result.output
        )

    @patch('opnsense_cli.commands.plugin.haproxy.errorfile.ApiClient.execute')
    def test_delete_NOT_FOUND(self, api_response_mock: Mock):
        result = self._opn_cli_command_result(
            api_response_mock,
            [
                self._api_data_fixtures_delete_NOT_FOUND,
                self._api_data_fixtures_configtest_OK,
                self._api_data_fixtures_reconfigure_OK,
            ],
            errorfile,
            [
                "delete", "99282721-934c-42be-ba4d-a93cbfda2644",
            ]
        )

        self.assertIn("Error: {'result': 'not found'}\n", result.output)
        self.assertEqual(1, result.exit_code)
