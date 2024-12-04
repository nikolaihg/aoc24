import System.IO

getLines = lines $ contents 

part1 = undefined
part2 = undefined

main :: IO ()
main = do
    contents <- readFile "C:\\Users\\nikol\\Desktop\\aoc24\\day01\\example.txt"
    putStrLn getLines contents 
