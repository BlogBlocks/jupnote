#! /usr/bin/ruby

require 'sqlite3'
require 'fileutils'

script_dir = File.dirname(File.expand_path(__FILE__))

# get original data
puts "Loading original data..."
input_db = "#{script_dir}/HelpIndex.db"
db0 = SQLite3::Database.new(input_db)
data = db0.execute( "select * from data" )

# rowids = `echo 'SELECT rowid FROM data;' | sqlite3 '#{input_db}'`.split(/\n/)
# data = []
# rowids.each do |rowid|
#   url     = `echo 'SELECT url     FROM data WHERE rowid = #{rowid};' | sqlite3 '#{input_db}'`
#   subject = `echo 'SELECT subject FROM data WHERE rowid = #{rowid};' | sqlite3 '#{input_db}'`
#   body    = `echo 'SELECT body    FROM data WHERE rowid = #{rowid};' | sqlite3 '#{input_db}'`
#   data.push({ :url => url, :subject => subject, :body => body})
# end
# puts data[0][0]
# puts data[0][1]
# puts data[0][2]
# puts data

# create contentful index with identical content
puts "Creating contentful index with 1x data..."
output_db1 = "#{script_dir}/index1.db"
FileUtils.rm output_db1, :force => true
db1 = SQLite3::Database.new(output_db1)
db1.execute("CREATE VIRTUAL TABLE data USING fts4(url, subject, body);")
data.each do |row_info|
  url     =  row_info[0]
  subject =  row_info[1]
  body    =  row_info[2]
  db1.execute("INSERT INTO data(url, subject, body) VALUES(?, ?, ?);", url, subject, body);
end

# create contentless index with identical content
puts "Creating contentless index with 1x data..."
output_db2 = "#{script_dir}/index2.db"
FileUtils.rm output_db2, :force => true
db2 = SQLite3::Database.new(output_db2)
db2.execute("CREATE VIRTUAL TABLE data USING fts4(content="", url, subject, body);")
db2.execute("CREATE TABLE info (url, subject);");
docid = 0
data.each do |row_info|
  url     =  row_info[0]
  subject =  row_info[1]
  body    =  row_info[2]
  db2.execute("INSERT INTO data(docid, url, subject, body) VALUES(?, ?, ?, ?);", docid, url, subject, body);
  db2.execute("INSERT INTO info(url, subject) VALUES(?, ?);", url, subject);
  docid += 1
end

# create contentful index with 10x content
puts "Creating contentful index with 10x data..."
output_db3 = "#{script_dir}/index3.db"
FileUtils.rm output_db3, :force => true
db3 = SQLite3::Database.new(output_db3)
db3.execute("CREATE VIRTUAL TABLE data USING fts4(url, subject, body);")
data.each do |row_info|
  # ["ab", "cd", "ef", "gh", "ij", "kl", "mn",
  (1..10).each do
    url     =  row_info[0]
    subject =  row_info[1]
    body    =  row_info[2]
    db3.execute("INSERT INTO data(url, subject, body) VALUES(?, ?, ?);", url, subject, body);
  end
end

# create contentless index with 10x content
puts "Creating contentless index with 10x data..."
output_db4 = "#{script_dir}/index4.db"
FileUtils.rm output_db4, :force => true
db4 = SQLite3::Database.new(output_db4)
db4.execute("CREATE VIRTUAL TABLE data USING fts4(content="", url, subject, body);")
db4.execute("CREATE TABLE info (url, subject);");
docid = 0
data.each do |row_info|
  (1..10).each do
    url     =  row_info[0]
    subject =  row_info[1]
    body    =  row_info[2]
    db4.execute("INSERT INTO data(docid, url, subject, body) VALUES(?, ?, ?, ?);", docid, url, subject, body);
    db4.execute("INSERT INTO info(url, subject) VALUES(?, ?);", url, subject);
    docid += 1
  end
end
