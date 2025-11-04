import time

def tocno_vrijeme():
    vrijeme = time.localtime()
    sati = vrijeme.tm_hour
    minute = vrijeme.tm_min
    sekunde = vrijeme.tm_sec
    return f"{sati}:{minute}:{sekunde}"

def main():
    print("Trenutno točno vrijeme je:", tocno_vrijeme())

if __name__ == "__main__":
    main()