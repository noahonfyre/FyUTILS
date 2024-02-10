package main

import (
	"context"
	"github.com/NoahOnFyre/gengine/filesystem"
	"io/fs"
	"os"
)

var (
	pathAliases = []PathAlias{
		{
			Short: "~",
			Path:  StripPath(homeDir),
		},
		{
			Short: "#",
			Path:  StripPath(mainDir),
		},
		{
			Short: "/",
			Path:  "C:\\",
		},
	}
)

func CheckUpdates() {
	release, _, err := githubClient.Repositories.GetLatestRelease(context.Background(), "noahonfyre", "FyUTILS")
	if err != nil {
		return
	}
	newestRelease = release
}

func CheckPaths(paths []string) int {
	pathsFixed := 0
	for _, path := range paths {
		if !filesystem.Exists(path) {
			err := os.Mkdir(path, fs.ModeDir)
			if err != nil {
				Error("Failed to create directory!")
				return pathsFixed
			}
			pathsFixed += 1
		}
	}
	return pathsFixed
}
