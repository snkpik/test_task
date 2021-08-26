from twirp.context import Context
from twirp.exceptions import TwirpServerException

import haberdasher_twirp, haberdasher_pb2

client = haberdasher_twirp.HaberdasherClient("http://localhost:3000")

# if you are using a custom prefix, then pass it as `server_path_prefix`
# param to `MakeHat` class.
try:
    response = client.MakeHatTest(ctx=Context(), request=haberdasher_pb2.Size(inches=12))
    print(response)
    response = client.GetDollarRate(ctx=Context(), request=haberdasher_pb2.Empty())
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())