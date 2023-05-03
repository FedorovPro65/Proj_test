import csv
import os, shutil, glob
import gzip
import zipfile
# Программа MyCopyFiles_2.py копирует
# архивные файлы в папку, заданную переменной master_dir
# затем распаковывает csv файл из архива в папку 'F:/IMSData/Russia_csv/Arh/'
# Обработка происходит по строкам файла File_List из папки master_dir

def mExtractArhFile(dir_from, dir_to, file_name_gz):
#Распаковывает архивный файл file_name_gz из папки dir_from в папку dir_to
    
    if file_name_gz[-2:] == 'gz' :  #Если gz архив
        file_name_csv = file_name_gz[:len(file_name_gz)-3]
        file_name_gz = dir_from + file_name_gz
        file_name_csv = dir_to  + file_name_csv
        #print(f'{file_name_gz} to {file_name_csv} .')
        with open(file_name_csv, 'wb') as f_out:
            with gzip.open(file_name_gz, 'rb') as f_in:
                shutil.copyfileobj(f_in, f_out)
    else: #Если zip архив
        file_name_gz = dir_from + file_name_gz
        file_name_csv = file_name_gz[:len(file_name_gz)-4] +'.csv'
        #print(f'{file_name_gz} to {file_name_csv} .')
        zipFile = zipfile.ZipFile(file_name_gz, 'r')
        zipFile.extractall(dir_to)
        zipFile.close()
    


master_dir = "F:/IMS_Downloads/Rus_csv/"
CSV_dir    = "F:/IMSData/Russia_csv/"
File_List  = master_dir + "File_List.csv"

with open(File_List, encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            # print(f'Файл содержит столбцы: {", ".join(row)}')
            print(f'Программа копирует архивные файлы IMS в папку {master_dir}')
            
        else:
            # Вывод строк
            s_Npp = ' ' + str(count)
            print(f' {s_Npp[-2:]} файл -  {row[2]}  {row[1]}  ')
            source_dir = row[2]
            File_Name = row[1]
            shutil.copy2(os.path.join(source_dir, File_Name), master_dir)
            # распаковывает csv файл из архива в папку 'F:/IMSData/Russia_csv/Arh/'
            mExtractArhFile(master_dir, CSV_dir, File_Name)
            
        count += 1
        #if count==6 :
        #        break
    print(f' Обработано {count-1} файлов.')
    txt = input("Нажмите Enter, для завершения программы ")
