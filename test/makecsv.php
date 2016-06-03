<?php
/*****-- カスタマイズ項目 --*****/
date_default_timezone_set('Asia/Tokyo');
set_time_limit(120);
$start = microtime( TRUE );
$visible_format = true;//true=表示、false=非表示

//
$csv_data_path = '/Applications/MAMP/htdocs/MyTest/csv/';
if (!file_exists ($csv_data_path)){
  mkdir ("$csv_data_path", 0777, true);
}
//
$datetime = date("Y_m_d_His");//{YYYY_MM_DD_HHMMSS}.csv
$csv_output_file = $csv_data_path . '/' . $datetime . '.csv';

//
$csv_format = array(
  #A
  '[ファイル名]',
  #B
  '[会員番号]',
  #C
  '[氏名_姓]',
  #D
  '[氏名_名]',
  #E
  '[氏名_セイ]',
  #F
  '[氏名_メイ]',
  #G
  '[生年月日]',
  #H
  '[性別]',
  #I
  '[法人名]',
  #J
  '[法人名_カナ]',
  #K
  '[役職]',
  #L
  '[役職_カナ]',
  #M
  '[郵便番号]',
  #N
  '[住所]',
  #O
  '[TEL_1]',
  #P
  '[TEL_2]',
  #Q
  '[TEL_3]',
  #R
  '[FAX_1]',
  #S
  '[FAX_2]',
  #T
  '[FAX_3]',
  #U
  '[携帯_1]',
  #V
  '[携帯_2]',
  #W
  '[携帯_3]',
  #X
  '[パスワード]',
  #Y
  '[口座_ゆうちょ]',
  #Z
  '[ゆうちょ_通帳記号]',
  #AA
  '[ゆうちょ_通帳番号]',
  #AB
  '[口座_銀行名]',
  #AC
  '[口座_店名]',
  #AD
  '[口座_預金種目]',
  #AE
  '[口座番号]',
  #AF
  '[紹介者会員番号]',
  #AG
  '[紹介者氏名_姓]',
  #AH
  '[紹介者氏名_名]',
  #AI
  '[紹介者氏名_セイ]',
  #AJ
  '[紹介者氏名_メイ]',
  #AK
  '[紹介ポジション]',
  #AL
  '[指定上位者会員番号]',
  #AM
  '[指定上位者氏名_姓]',
  #AN
  '[指定上位者氏名_名]',
  #AO
  '[指定上位者氏名_セイ]',
  #AP
  '[指定上位者氏名_メイ]',
  #AQ
  '[ライン]',
  #AR
  '[定期商品_商品番号_MC]',
  #AS
  '[定期商品_商品番号_MC_参照]',
  #AT
  '[定期商品_商品名_MC]',
  #AV
  '[定期商品_数量_MC]',
  #AU
  '[定期商品_商品番号_BC1]',
  #AW
  '[定期商品_商品番号_BC1_参照]',
  #AX
  '[定期商品_商品名_BC1]',
  #AY
  '[定期商品_数量_BC1]',
  #AZ
  '[定期商品_商品番号_BC2]',
  #BA
  '[定期商品_商品番号_BC2_参照]',
  #BB
  '[定期商品_商品名_BC2]',
  #BC
  '[定期商品_数量_BC2]',
  #BD
  '[初回商品_商品番号]',
  #BE
  '[初回商品_商品番号_参照]',
  #BF
  '[初回商品_商品名]',
  #BG
  '[初回商品_数量]',
  #BH
  '[支払方法]',
  #BI
  '[支払方法_カード番号]',
  #BJ
  '[支払方法_カード名義人]',
  #BK
  '[支払方法_カード有効期限]',
  #BL
  '[商品配送先_郵便番号]',
  #BM
  '[商品配送先_住所]',
  #BN
  '[商品配送先_宛先]',
  #BO
  '[商品配送先_TEL_1]',
  #BP
  '[商品配送先_TEL_2]',
  #BQ
  '[商品配送先_TEL_3]');

//
#mb_convert_variables('SJIS','UTF-8',$csv_format);
$array[$document_id]["format"] = $csv_format;

try{
  //csvファイルオープン
  $fp = fopen($csv_output_file,'w');
  //1行め目の項目を入力（表示の設定なら）
  if($visible_format){
    fputcsv($fp, $array[$document_id]["format"]);
  }

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
    $csv_list[$row['document_id']][] = $row['uri'];
    //resultを設定
    $array[$row['document_id']][$row['uri']][$row['entry_id']] = $row['result'];//mb_convert_encoding($row['result'], 'SJIS', 'UTF-8');
  }

  //重複を取り除く
  foreach ($csv_list as $key => $value) {
    $csv_list[$key] = array_unique($csv_list[$key]);
  }

  //csvファイルを生成
  if( $csv_output_file ){
    //
    foreach ($csv_list as $csv_key => $csv_value){
      foreach ($csv_value as $key => $value) {
        fputcsv($fp, $array[$csv_key][$value]);
      }
    }
  }
  //csvファイルをクローズ
  fclose($fp);

  //csv生成が完了したら、DBのstatusを更新
  try {
    $dbh->beginTransaction();
    //
    foreach ($csv_list as $csv_key => $csv_value){
      foreach ($csv_value as $key => $value) {
        $update_sql = 'UPDATE transaction_cropped SET status = 2 WHERE document_id = ' . $csv_key . ' AND ' . 'uri = \'' . $value . '\'';
        echo $update_sql . "\n";
        $dbh->query($update_sql);
      }
    }
    $dbh->commit();

    //NXへ通知
    //code

  } catch (Exception $e) {
    $dbh->rollBack();
    print('DB update Failed: ' . $e->getMessage());
  }
} catch (PDOException $e){
    print('Error:'.$e->getMessage());
    die();
}

//
$dbh = null;

?>
