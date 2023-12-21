API_KEY: 277b561d99678f9dfff978ae65b8ce36
API_SECRET: 4f5fef188468aec17c36e7f46a319a5cc664fd0ab6681d3c8028ae2acb88dbbe
Traceback (most recent call last):
  File "c:\Users\avets\Documents\market_scrapper\gateio_api\app.py", line 17, in <module>
    schedule.run_pending()
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\schedule\__init__.py", line 822, in run_pending
    default_scheduler.run_pending()
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\schedule\__init__.py", line 100, in run_pending
    self._run_job(job)
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\schedule\__init__.py", line 172, in _run_job
    ret = job.run()
          ^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\schedule\__init__.py", line 693, in run
    ret = self.job_func()
          ^^^^^^^^^^^^^^^
  File "c:\Users\avets\Documents\market_scrapper\gateio_api\app.py", line 10, in updateListFuturesContract
    result = listFuturesContracts()
             ^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\avets\Documents\market_scrapper\gateio_api\api_calls.py", line 42, in listFuturesContracts
    list_futures_contract = api_futures_instance.list_futures_contracts(settle)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\api\futures_api.py", line 58, in list_futures_contracts
    return self.list_futures_contracts_with_http_info(settle, **kwargs)  # noqa: E501
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\api\futures_api.py", line 122, in list_futures_contracts_with_http_info
    return self.api_client.call_api(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\api_client.py", line 394, in call_api
    return self.__call_api(
           ^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\api_client.py", line 189, in __call_api
    response_data = self.request(
                    ^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\api_client.py", line 446, in request
    return self.rest_client.GET(
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\rest.py", line 237, in GET
    return self.request(
           ^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\gate_api\rest.py", line 218, in request
    r = self.pool_manager.request(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\urllib3\_request_methods.py", line 110, in request
    return self.request_encode_url(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\urllib3\_request_methods.py", line 143, in request_encode_url
    return self.urlopen(method, url, **extra_kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\urllib3\poolmanager.py", line 433, in urlopen
    conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\urllib3\poolmanager.py", line 304, in connection_from_host
    return self.connection_from_context(request_context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\avets\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\urllib3\poolmanager.py", line 326, in connection_from_context
    raise URLSchemeUnknown(scheme)
urllib3.exceptions.URLSchemeUnknown: Not supported URL scheme amqp