import AminoLab
import concurrent.futures
from AminoLab.utils.objects import ChatThreads
client = AminoLab.Client()
client.auth(email="vy32ds4@esiix.com", password="12345678")
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
	print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> "))-1]
chats = client.get_public_chat_threads(ndc_Id, size="100")
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
threadId = chats.thread_Id[int(input("Select The Chat >> "))-1]
def join():
    client.edit_profile(ndc_Id,nickname="ban hojaeyga")
    client.leave_thread(ndc_Id,threadId)
    client.join_thread(ndc_Id,threadId)
    client.leave_thread(ndc_Id,threadId)
    client.join_thread(ndc_Id,threadId)
    client.leave_thread(ndc_Id,threadId)
    client.join_thread(ndc_Id,threadId)
    client.leave_thread(ndc_Id,threadId)
    client.join_thread(ndc_Id_,threadId)

while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        _ = [executor.submit(join) for _ in range(9000)]
# while True:
#     thread()