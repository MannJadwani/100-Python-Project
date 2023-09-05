import speedtest

test = speedtest.Speedtest()

print('Loading Server List...')

test.get_servers()

print('finding best server')

best = test.get_best_server()
print(f'Found {best["host"]}')

print('Peforming Download test..')

downloadResult = test.download()

print('Peforming Upload test..')

uploadResult = test.upload()

pingResult = test.results.ping

print(f'Download-Speed: {(downloadResult/1024)/1024 :.2f} mbps')
print(f'Upload-Speed: {(uploadResult/1024)/1024 :.2f} mbps')
print(f'Latency: {pingResult} ms')



