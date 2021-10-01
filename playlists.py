import sqlite3
from pathlib import Path
import os
from typing import List


class PlaylistManager:
    """
    Manages user playlists.
    """

    def __init__(self) -> None:
        self.homedir = (Path.home()) / ".powerplayer"
        os.makedirs(self.homedir, exist_ok=True)

        self.db = sqlite3.connect(self.homedir / "playlists.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY, name TEXT, songs TEXT)"
        )
        self.db.commit()

    def __enter__(self) -> "PlaylistManager":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.db.close()

    def add_playlist(self, name: str, songs: List[str]) -> None:
        """
        Adds a playlist to the database.
        """
        self.cursor.execute(
            "INSERT INTO playlists (name, songs) VALUES (?, ?)", (name, ",".join(songs))
        )
        self.db.commit()

    def get_all_playlists(self) -> List[str]:
        """
        Returns a list of all playlists.
        """
        self.cursor.execute("SELECT name FROM playlists")
        return [row[0] for row in self.cursor.fetchall()]

    def get_playlist_songs(self, name: str) -> List[str]:
        """
        Returns a list of all songs in a playlist.
        """
        self.cursor.execute("SELECT songs FROM playlists WHERE name = ?", (name,))
        return [song for song in self.cursor.fetchone()[0].split(",")]

    def edit_playlist(self, name: str, songs: List[str]) -> None:
        """
        Edits a playlist.
        """
        self.cursor.execute(
            "UPDATE playlists SET songs = ? WHERE name = ?", (",".join(songs), name)
        )
        self.db.commit()
