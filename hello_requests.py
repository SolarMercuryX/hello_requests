import requests
import time

def main():
    print('Hello World !')

    # res = requests.get('https://api.github.com/events')
    # print(res.status_code)
    # print(res.headers['content-type'])
    # print(res.encoding)
    # print(res.text)
    # res.json()

    # res = requests.post('https://httpbin.org/post', data = {'key':'value'})
    # print(res.text)
    # res = requests.put('https://httpbin.org/put', data = {'key':'value'})
    # print(res.text)
    # res = requests.delete('https://httpbin.org/delete')
    # print(res.text)
    # res = requests.head('https://httpbin.org/head')
    # print(res.text)
    # res = requests.options('https://httpbin.org/options')
    # print(res.text)

    # payload = {'key1' : 'value1', 'key2' : 'value2'}
    # res = requests.get('https://httpbin.org/get', params=payload)
    # print(res.text)
    # payload = {'key1' : 'value1', 'key2' : ['value2', 'value3']}
    # res = requests.get('https://httpbin.org/get', params=payload)
    # print(res.text)

    # headers = {'user-agent' : 'my-app/0.0.1'}
    # res = requests.get('https://httpbin.org/headers', headers=headers)
    # print(res.text)
    # print(res.request.headers)
    # print(res.headers)

if __name__ == '__main__':
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f'[Finished in {(end_time - start_time):.1f}s]')
