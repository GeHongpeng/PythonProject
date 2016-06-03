<?php
/*****-- カスタマイズ項目 --*****/
date_default_timezone_set('Asia/Tokyo');
set_time_limit(120);
$start = microtime( TRUE );

$output_file_path = '/Applications/MAMP/htdocs/';
$datetime = date("Y_m_d_His");//{YYYY_MM_DD_HHMMSS}.txt
$output_file = $output_file_path . 'MyTest/txt/' . $datetime . '.txt';
$warnning_list = null;

//warnning format
$file_format = array(
  '[document_id]',
  '[uri]',
  '[entry_id]',
  '[message]'
);

//バリデーション処理
function validate($document_id, $uri, $entry_id, $result)
{
  global $warnning_list;

  $target_result = '';
  switch($entry_id){
    case 'A':
        $target_result = $result;
        //
        $warnning_list[$document_id][$uri][$entry_id] = 'A-converted!';
        break;
    case 'B':
        $target_result = $result;
        break;
    default:
        $target_result = $result;
  }

  return $target_result;
}

//
#mb_convert_variables('SJIS','UTF-8',$file_format);
$array[$document_id]["format"] = $file_format;

//
try{
  //ファイルオープン
  $fp = fopen($output_file,'w');
  fputcsv($fp, $array[$document_id]["format"]);

  //DBアクセスのパラメタを設定
  $dsn = 'mysql:host=127.0.0.1;dbname=test';
  $username = 'root';
  $password = 'root';
  $options = array(
      PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8',
  );

  //DBを接続
  $dbh = new PDO($dsn, $username, $password, $options)
    or die('Error connecting to MySQL server.');

  //クエリ文字列を作成
  $sql_target = 'SELECT id, document_id, entry_id, uri, result FROM transaction_cropped WHERE status = 1';

  //クエリ処理を実行
  foreach ($dbh->query($sql_target) as $row) {
    //処理対象リストにuriを追加
    #$warnning_list[$row['document_id']][] = $row['uri'];
    //バリデーション処理を実施
    $array[$row['document_id']][$row['uri']][$row['entry_id']] = validate($row['document_id'], $row['uri'], $row['entry_id'], $row['result']);//mb_convert_encoding($row['result'], 'SJIS', 'UTF-8');
  }

  //txtファイルを生成
  if( $output_file ){
    fwrite($fp, var_export($warnning_list, TRUE));
    //
    /*
    foreach ($warnning_list as $document_key => $document_value){
      foreach ($warnning_list[$document_key] as $uri_key => $uri_value){
        foreach ($warnning_list[$document_key][$uri_key] as $entry_key => $entry_value) {
          $message = $document_key . ' ' . $uri_key . ' ' . $entry_key . ' ' . $entry_value . "\n";
          //fwrite($fp, $message);
        }
      }
    }
    */
  }

  //ファイルをクローズ
  fclose($fp);
} catch (PDOException $e){
    print('Error:'.$e->getMessage());
    die();
}

//
$dbh = null;

?>
