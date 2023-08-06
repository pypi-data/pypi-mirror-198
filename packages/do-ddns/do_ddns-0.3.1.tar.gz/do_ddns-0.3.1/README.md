# DDNS

_DDNS_ is a dynamic DNS helper for Digital Ocean users to utilize their DO account as a Dynamic DNS resolver.

## Installation

Copy the ```ddns.py``` file to e.g. ```/usr/local/bin``` folder and run ```chmod +x``` to make it executable. You can remove the .py filending if you wish.

Run ```pip3 install -r requirements.txt``` to install all requirements the app needs.

## Usage

For instructions run 

```bash
ddns -h
```

The program is best suited to be executed with e.g cron or any other system that can run at intervals. To run the app every 6 hours with cron add the following line to your crontab

```bash
0 */6 * * *  /usr/local/bin/ddns
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Support

If you found a bug or you have sugestion for new features create an issue.

## Future development

- [ ] IPv6 support
- [ ] Add and delete non existing (new) domains to DO account

## License

[<img src="https://www.gnu.org/graphics/gplv3-with-text-136x68.png">](https://www.gnu.org/licenses/gpl-3.0.en.html)
