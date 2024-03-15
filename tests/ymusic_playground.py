import ytmusicapi


def main():
    ytm = ytmusicapi.YTMusic("/Users/ajanistewart/gh/spot2ytmusic/oauth.json")
    print("My playlists:")
    my_playlist = ytm.get_playlist("PLyjYzUHM3SuuH9GUbgbSZHF1E4YVks3T5") # my playlist
    # not_mine_playlist = ytm.get_playlist("PLaZPMsuQNCsWn0iVMtGbaUXO6z-EdZaZm") # someone else's playlist
# try:
    #     print("Not my playlist:")
    # except Exception as e:
    #     print(e)



if __name__ == "__main__":
    main()
