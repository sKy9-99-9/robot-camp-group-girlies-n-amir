import java.nio.file.{Files, Paths}
import scala.util.Try

object Main {
  def main(args: Array[String]): Unit = {
    val inputPath = "../fulldata/data5.txt"
    val outputPath = "../fulldata/data6.txt"
    val lines = scala.io.Source.fromFile(inputPath).getLines().toList
    val outputLines = lines.zipWithIndex.map {
      case (line, 0) => s"$line,Comments"
      case (line, _) =>
        val parts = line.split(",").map(_.trim)
        if (parts.length < 8) line
        else {
          val summary = parts(6)
          val evaluation = Try(parts(7).toFloat).getOrElse(0.0f)
          val comments = (summary, evaluation) match {
            case ("super", e) if e >= 3 => "Excellent"
            case ("super", _) => "Good but inconsistent"
            case (_, e) if e >= 2 => "Promising"
            case _ => "Needs Improvement"
          }
          s"$line,$comments"
        }
    }

    Files.write(Paths.get(outputPath), outputLines.mkString("\n").getBytes)
    println(s"Processed ${lines.length - 1} lines. Output written to $outputPath")
  }
}
